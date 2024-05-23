# ruff: noqa: E402
# Copyright (c) Microsoft Corporation. All rights reserved.
"""Implementation of tool support over LSP."""

from __future__ import annotations

import copy
import json
import os
import pathlib
import sys
import traceback
from typing import Any, Optional, Sequence


# **********************************************************
# Update sys.path before importing any bundled libraries.
# **********************************************************
def update_sys_path(path_to_add: str, strategy: str) -> None:
    """Add given path to `sys.path`."""
    if path_to_add not in sys.path and os.path.isdir(path_to_add):
        if strategy == "useBundled":
            sys.path.insert(0, path_to_add)
        elif strategy == "fromEnvironment":
            sys.path.append(path_to_add)


# Ensure that we can import LSP libraries, and other bundled libraries.
update_sys_path(
    os.fspath(pathlib.Path(__file__).parent.parent / "libs"),
    os.getenv("LS_IMPORT_STRATEGY", "useBundled"),
)

# **********************************************************
# Imports needed for the language server go below this.
# **********************************************************
# pylint: disable=wrong-import-position,import-error
import lsp_jsonrpc as jsonrpc
import lsp_utils as utils
import lsprotocol.types as lsp
from pygls import server, uris, workspace

# version of python we are running
# print("Python version: ", sys.version)

# Log the sys.path used to run the server.
# print("sys.path used to run Server: ", sys.path)

# log all available python packages
# print("Available python packages: ", os.listdir(sys.path[0]))

from package.ai.crew import (
    improve_code,
)  # Adjust the import based on your package structure

WORKSPACE_SETTINGS = {}
GLOBAL_SETTINGS = {}
RUNNER = pathlib.Path(__file__).parent / "lsp_runner.py"

MAX_WORKERS = 5
# TODO: Update the language server name and version.
LSP_SERVER = server.LanguageServer(
    name="llm-swarm", version="<server version>", max_workers=MAX_WORKERS
)

# **********************************************************
# Tool-specific code goes below this.
# **********************************************************

# TODO: Update TOOL_MODULE with the module name for your tool.
# e.g, TOOL_MODULE = "pylint"
TOOL_MODULE = "llm-swarm"

# TODO: Update TOOL_DISPLAY with a display name for your tool.
# e.g, TOOL_DISPLAY = "Pylint"
TOOL_DISPLAY = "LLM Swarm"

# TODO: Update TOOL_ARGS with default arguments you have to pass to your tool in all scenarios.
TOOL_ARGS = []  # default arguments always passed to your tool.


# **********************************************************
# Required Language Server Initialization and Exit handlers.
# **********************************************************
@LSP_SERVER.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams) -> None:
    """LSP handler for initialize request."""
    log_to_output(f"CWD Server: {os.getcwd()}")

    paths = "\r\n   ".join(sys.path)
    log_to_output(f"sys.path used to run Server:\r\n   {paths}")

    GLOBAL_SETTINGS.update(**params.initialization_options.get("globalSettings", {}))

    settings = params.initialization_options["settings"]
    _update_workspace_settings(settings)
    log_to_output(
        f"Settings used to run Server:\r\n{json.dumps(settings, indent=4, ensure_ascii=False)}\r\n"
    )
    log_to_output(
        f"Global settings:\r\n{json.dumps(GLOBAL_SETTINGS, indent=4, ensure_ascii=False)}\r\n"
    )


@LSP_SERVER.feature(lsp.EXIT)
def on_exit(_params: Optional[Any] = None) -> None:
    """Handle clean up on exit."""
    jsonrpc.shutdown_json_rpc()


@LSP_SERVER.feature(lsp.SHUTDOWN)
def on_shutdown(_params: Optional[Any] = None) -> None:
    """Handle clean up on shutdown."""
    jsonrpc.shutdown_json_rpc()


def _get_global_defaults():
    return {
        "path": GLOBAL_SETTINGS.get("path", []),
        "interpreter": GLOBAL_SETTINGS.get("interpreter", [sys.executable]),
        "args": GLOBAL_SETTINGS.get("args", []),
        "importStrategy": GLOBAL_SETTINGS.get("importStrategy", "useBundled"),
        "showNotifications": GLOBAL_SETTINGS.get("showNotifications", "off"),
    }


def _update_workspace_settings(settings):
    if not settings:
        key = os.getcwd()
        WORKSPACE_SETTINGS[key] = {
            "cwd": key,
            "workspaceFS": key,
            "workspace": uris.from_fs_path(key),
            **_get_global_defaults(),
        }
        return

    for setting in settings:
        key = uris.to_fs_path(setting["workspace"])
        WORKSPACE_SETTINGS[key] = {
            "cwd": key,
            **setting,
            "workspaceFS": key,
        }


def _get_settings_by_path(file_path: pathlib.Path):
    workspaces = {s["workspaceFS"] for s in WORKSPACE_SETTINGS.values()}

    while file_path != file_path.parent:
        str_file_path = str(file_path)
        if str_file_path in workspaces:
            return WORKSPACE_SETTINGS[str_file_path]
        file_path = file_path.parent

    setting_values = list(WORKSPACE_SETTINGS.values())
    return setting_values[0]


def _get_document_key(document: workspace.Document):
    if WORKSPACE_SETTINGS:
        document_workspace = pathlib.Path(document.path)
        workspaces = {s["workspaceFS"] for s in WORKSPACE_SETTINGS.values()}

        # Find workspace settings for the given file.
        while document_workspace != document_workspace.parent:
            if str(document_workspace) in workspaces:
                return str(document_workspace)
            document_workspace = document_workspace.parent

    return None


def _get_settings_by_document(document: workspace.Document | None):
    if document is None or document.path is None:
        return list(WORKSPACE_SETTINGS.values())[0]

    key = _get_document_key(document)
    if key is None:
        # This is either a non-workspace file or there is no workspace.
        key = os.fspath(pathlib.Path(document.path).parent)
        return {
            "cwd": key,
            "workspaceFS": key,
            "workspace": uris.from_fs_path(key),
            **_get_global_defaults(),
        }

    return WORKSPACE_SETTINGS[str(key)]


# *****************************************************
# Internal execution APIs.
# *****************************************************
def _run_tool_on_document(
    document: workspace.Document,
    use_stdin: bool = False,
    extra_args: Optional[Sequence[str]] = None,
) -> utils.RunResult | None:
    """Runs tool on the given document.

    if use_stdin is true then contents of the document is passed to the
    tool via stdin.
    """
    if extra_args is None:
        extra_args = []
    if str(document.uri).startswith("vscode-notebook-cell"):
        # TODO: Decide on if you want to skip notebook cells.
        # Skip notebook cells
        return None

    if utils.is_stdlib_file(document.path):
        # TODO: Decide on if you want to skip standard library files.
        # Skip standard library python files.
        return None

    # deep copy here to prevent accidentally updating global settings.
    settings = copy.deepcopy(_get_settings_by_document(document))

    code_workspace = settings["workspaceFS"]
    cwd = settings["cwd"]

    use_path = False
    use_rpc = False
    if settings["path"]:
        # 'path' setting takes priority over everything.
        use_path = True
        argv = settings["path"]
    elif settings["interpreter"] and not utils.is_current_interpreter(
        settings["interpreter"][0]
    ):
        # If there is a different interpreter set use JSON-RPC to the subprocess
        # running under that interpreter.
        argv = [TOOL_MODULE]
        use_rpc = True
    else:
        # if the interpreter is same as the interpreter running this
        # process then run as module.
        argv = [TOOL_MODULE]

    argv += TOOL_ARGS + settings["args"] + extra_args

    if use_stdin:
        # TODO: update these to pass the appropriate arguments to provide document contents
        # to tool via stdin.
        # For example, for pylint args for stdin looks like this:
        #     pylint --from-stdin <path>
        # Here `--from-stdin` path is used by pylint to make decisions on the file contents
        # that are being processed. Like, applying exclusion rules.
        # It should look like this when you pass it:
        #     argv += ["--from-stdin", document.path]
        # Read up on how your tool handles contents via stdin. If stdin is not supported use
        # set use_stdin to False, or provide path, what ever is appropriate for your tool.
        argv += []
    else:
        argv += [document.path]

    if use_path:
        # This mode is used when running executables.
        log_to_output(" ".join(argv))
        log_to_output(f"CWD Server: {cwd}")
        result = utils.run_path(
            argv=argv,
            use_stdin=use_stdin,
            cwd=cwd,
            source=document.source.replace("\r\n", "\n"),
        )
        if result.stderr:
            log_to_output(result.stderr)
    elif use_rpc:
        # This mode is used if the interpreter running this server is different from
        # the interpreter used for running this server.
        log_to_output(" ".join(settings["interpreter"] + ["-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")

        result = jsonrpc.run_over_json_rpc(
            workspace=code_workspace,
            interpreter=settings["interpreter"],
            module=TOOL_MODULE,
            argv=argv,
            use_stdin=use_stdin,
            cwd=cwd,
            source=document.source,
        )
        if result.exception:
            log_error(result.exception)
            result = utils.RunResult(result.stdout, result.stderr)
        elif result.stderr:
            log_to_output(result.stderr)
    else:
        # In this mode the tool is run as a module in the same process as the language server.
        log_to_output(" ".join([sys.executable, "-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")
        # This is needed to preserve sys.path, in cases where the tool modifies
        # sys.path and that might not work for this scenario next time around.
        with utils.substitute_attr(sys, "path", sys.path[:]):
            try:
                # TODO: `utils.run_module` is equivalent to running `python -m <pytool-module>`.
                # If your tool supports a programmatic API then replace the function below
                # with code for your tool. You can also use `utils.run_api` helper, which
                # handles changing working directories, managing io streams, etc.
                # Also update `_run_tool` function and `utils.run_module` in `lsp_runner.py`.
                result = utils.run_module(
                    module=TOOL_MODULE,
                    argv=argv,
                    use_stdin=use_stdin,
                    cwd=cwd,
                    source=document.source,
                )
            except Exception:
                log_error(traceback.format_exc(chain=True))
                raise
        if result.stderr:
            log_to_output(result.stderr)

    log_to_output(f"{document.uri} :\r\n{result.stdout}")
    return result


def _run_tool(extra_args: Sequence[str]) -> utils.RunResult:
    """Runs tool."""
    # deep copy here to prevent accidentally updating global settings.
    settings = copy.deepcopy(_get_settings_by_document(None))

    code_workspace = settings["workspaceFS"]
    cwd = settings["workspaceFS"]

    use_path = False
    use_rpc = False
    if len(settings["path"]) > 0:
        # 'path' setting takes priority over everything.
        use_path = True
        argv = settings["path"]
    elif len(settings["interpreter"]) > 0 and not utils.is_current_interpreter(
        settings["interpreter"][0]
    ):
        # If there is a different interpreter set use JSON-RPC to the subprocess
        # running under that interpreter.
        argv = [TOOL_MODULE]
        use_rpc = True
    else:
        # if the interpreter is same as the interpreter running this
        # process then run as module.
        argv = [TOOL_MODULE]

    argv += extra_args

    if use_path:
        # This mode is used when running executables.
        log_to_output(" ".join(argv))
        log_to_output(f"CWD Server: {cwd}")
        result = utils.run_path(argv=argv, use_stdin=True, cwd=cwd)
        if result.stderr:
            log_to_output(result.stderr)
    elif use_rpc:
        # This mode is used if the interpreter running this server is different from
        # the interpreter used for running this server.
        log_to_output(" ".join(settings["interpreter"] + ["-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")
        result = jsonrpc.run_over_json_rpc(
            workspace=code_workspace,
            interpreter=settings["interpreter"],
            module=TOOL_MODULE,
            argv=argv,
            use_stdin=True,
            cwd=cwd,
        )
        if result.exception:
            log_error(result.exception)
            result = utils.RunResult(result.stdout, result.stderr)
        elif result.stderr:
            log_to_output(result.stderr)
    else:
        # In this mode the tool is run as a module in the same process as the language server.
        log_to_output(" ".join([sys.executable, "-m"] + argv))
        log_to_output(f"CWD Linter: {cwd}")
        # This is needed to preserve sys.path, in cases where the tool modifies
        # sys.path and that might not work for this scenario next time around.
        with utils.substitute_attr(sys, "path", sys.path[:]):
            try:
                # TODO: `utils.run_module` is equivalent to running `python -m <pytool-module>`.
                # If your tool supports a programmatic API then replace the function below
                # with code for your tool. You can also use `utils.run_api` helper, which
                # handles changing working directories, managing io streams, etc.
                # Also update `_run_tool_on_document` function and `utils.run_module` in `lsp_runner.py`.
                result = utils.run_module(
                    module=TOOL_MODULE, argv=argv, use_stdin=True, cwd=cwd
                )
            except Exception:
                log_error(traceback.format_exc(chain=True))
                raise
        if result.stderr:
            log_to_output(result.stderr)

    log_to_output(f"\r\n{result.stdout}\r\n")
    return result


# *****************************************************
# Logging and notification.
# *****************************************************
def log_to_output(
    message: str, msg_type: lsp.MessageType = lsp.MessageType.Log
) -> None:
    LSP_SERVER.show_message_log(message, msg_type)


def log_error(message: str) -> None:
    LSP_SERVER.show_message_log(message, lsp.MessageType.Error)
    if os.getenv("LS_SHOW_NOTIFICATION", "off") in ["onError", "onWarning", "always"]:
        LSP_SERVER.show_message(message, lsp.MessageType.Error)


def log_warning(message: str) -> None:
    LSP_SERVER.show_message_log(message, lsp.MessageType.Warning)
    if os.getenv("LS_SHOW_NOTIFICATION", "off") in ["onWarning", "always"]:
        LSP_SERVER.show_message(message, lsp.MessageType.Warning)


def log_always(message: str) -> None:
    LSP_SERVER.show_message_log(message, lsp.MessageType.Info)
    if os.getenv("LS_SHOW_NOTIFICATION", "off") in ["always"]:
        LSP_SERVER.show_message(message, lsp.MessageType.Info)


# *****************************************************
# Command handlers and utility functions.
# *****************************************************


# Command handler for 'llm_swarm_ai_improve_file'
@LSP_SERVER.command("llm_swarm_ai_improve_file")
def llm_swarm_ai_improve_file(ls: server.LanguageServer, arguments: Any):
    log_to_output("Running 'llm_swarm_ai_improve_file' command.")
    if arguments and "uri" in arguments[0]:
        uri = arguments[0]["uri"]
        document = ls.workspace.get_text_document(uri)
        if document:
            edits = improve_code_with_llm_swarm(document)
            if edits:
                apply_text_edits(ls, uri, edits, document.version)
            else:
                log_to_output("No changes were made to the document.")
        else:
            log_to_output(f"Document not found or already disposed. URI: {uri}")
    else:
        log_to_output("Invalid arguments for 'llm_swarm_ai_improve_file' command.")


# Command handler for 'llm_swarm_ai_improve_selection'
@LSP_SERVER.command("llm_swarm_ai_improve_selection")
def llm_swarm_ai_improve_selection(ls: server.LanguageServer, arguments: Any):
    log_to_output("Running 'llm_swarm_ai_improve_selection' command.")
    if arguments and "uri" in arguments[0] and "range" in arguments[0]:
        uri = arguments[0]["uri"]
        range = arguments[0]["range"]
        document = ls.workspace.get_text_document(uri)
        if document:
            selected_text = document.source[
                range["start"]["line"] : range["end"]["line"]
            ]
            edits = improve_selected_text_with_llm_swarm(document, selected_text, range)
            if edits:
                apply_text_edits(ls, uri, edits, document.version)
            else:
                log_to_output("No changes were made to the selection.")
        else:
            log_to_output(f"Document not found or already disposed. URI: {uri}")
    else:
        log_to_output("Invalid arguments for 'llm_swarm_ai_improve_selection' command.")


# Function to apply text edits to a document
def apply_text_edits(
    ls: server.LanguageServer, uri: str, edits: list[lsp.TextEdit], version: int
):
    log_to_output("Applying text edits to document.")

    # Verify and log edits (briefly)
    for edit in edits:
        log_to_output(
            f"Edit Range: Start({edit.range.start.line},{edit.range.start.character}) "
            f"End({edit.range.end.line},{edit.range.end.character}) "
            f"New Text: {edit.new_text[:30]}..."
        )

    # Create VersionedTextDocumentIdentifier and TextDocumentEdit
    versioned_text_document_identifier = lsp.VersionedTextDocumentIdentifier(
        uri=uri, version=version
    )
    text_document_edit = lsp.TextDocumentEdit(
        text_document=versioned_text_document_identifier, edits=edits
    )

    # Create WorkspaceEdit and apply the edit
    workspace_edit = lsp.WorkspaceEdit(document_changes=[text_document_edit])
    response = ls.apply_edit(workspace_edit)

    # Define callback function for handling the result
    def on_applied(future):
        try:
            result = future.result()
            log_to_output(f"Edit applied result: {result}")
            if not result.applied:
                handle_edit_failure(result, edits)
        except Exception as e:
            log_to_output(f"Failed to apply edit: {e}", lsp.MessageType.Error)

    response.add_done_callback(on_applied)

    log_to_output(f"Response from apply_edit: {response}")


def log_error_context(edits):
    for edit in edits:
        log_to_output(
            f"Edit Range: {edit.range.start.line}:{edit.range.start.character} to {edit.range.end.line}:{edit.range.end.character}"
        )
        log_to_output(f"New Text: {edit.new_text}")


# Function to handle edit failures
def handle_edit_failure(result, edits):
    log_error(f"Failed to apply edit: {result.failure_reason}")
    if result.failed_change:
        log_error(f"Failed change: {result.failed_change}")
    for edit in edits:
        log_error(
            f"Edit Range: {edit.range.start.line}:{edit.range.start.character} to "
            f"{edit.range.end.line}:{edit.range.end.character}"
        )
        log_error(f"New Text: {edit.new_text}")


# Function to improve code with llm_swarm
def improve_code_with_llm_swarm(
    document: workspace.Document,
) -> list[lsp.TextEdit] | None:
    log_to_output("Improving code with llm_swarm.")
    try:
        improved_code = improve_code(document.source, verbose=0)
        if document.source != improved_code:
            edit = lsp.TextEdit(
                range=lsp.Range(
                    start=lsp.Position(line=0, character=0),
                    end=lsp.Position(line=len(document.lines), character=0),
                ),
                new_text=improved_code,
            )
            return [edit]
        return None
    except Exception as e:
        log_to_output(
            f"Error occurred while improving code: {e}", lsp.MessageType.Error
        )
        return None


# Function to improve selected text with llm_swarm
def improve_selected_text_with_llm_swarm(
    document: workspace.Document, selected_text: str, range: dict
) -> list[lsp.TextEdit] | None:
    log_to_output("Improving selected text with llm_swarm.")
    try:
        improved_code = improve_code(selected_text, verbose=0)
        if selected_text != improved_code:
            edit = lsp.TextEdit(
                range=lsp.Range(
                    start=lsp.Position(
                        line=range["start"]["line"],
                        character=range["start"]["character"],
                    ),
                    end=lsp.Position(
                        line=range["end"]["line"], character=range["end"]["character"]
                    ),
                ),
                new_text=improved_code,
            )
            return [edit]
        return None
    except Exception as e:
        log_to_output(
            f"Error occurred while improving selected text: {e}", lsp.MessageType.Error
        )
        return None


# *****************************************************
# Start the server.
# *****************************************************
if __name__ == "__main__":
    print("Starting LSP server.")
    LSP_SERVER.start_io()
