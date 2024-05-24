import subprocess
import time
import ollama
from langchain_community.llms import Ollama


def stop_ollama_server():
    """
    Stop the Ollama server.
    """
    # TODO: End process gracefully (currently there's no command to stop the server).
    subprocess.run(["pkill", "ollama"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Ollama server stopped.")


def start_ollama_server() -> bool:
    """
    Start the Ollama server.

    Returns:
        bool: True if the server was started successfully, False otherwise.
    """
    # Stop the server if it is already running
    stop_ollama_server()

    try:
        # Start the ollama server (necessary for using the ollama package)
        # and let continue running in the background
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.PIPE,  # suppress output
            stderr=subprocess.PIPE,
            text=True,
        )
        # give the server some time to start
        time.sleep(3)

        print("Ollama server started.")
        return True

    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Ollama is not installed. Please visit https://ollama.com/.")
        return False


def is_model_locally_stored(model_name: str):
    """
    Check if the model exists locally.
    """
    return model_name in [model["name"] for model in ollama.list().get("models")]


def download_model(model_name: str) -> bool:
    """
    Download the model to local machine (saves to `~/.ollama/models` by default).

    Args:
        model_name (str): The name of the model to download.

    Returns:
        bool: True if the model was downloaded successfully or already exists, False otherwise.
    """
    try:
        print("Checking if model exists locally...")
        if not is_model_locally_stored(model_name):
            print(f"Downloading model {model_name}...")
            ollama.pull(model_name)
        else:
            print(f"Model {model_name} already exists locally.")
        return True
    except Exception:
        print(f"Ollama error: model {model_name} could not be retrieved.")
        return False


TEST_INPUT_CODE = """
def findMin (L,startIndx):
    m = L[startIndx]
    index = startIndx
    for i in range (startIndx,len(L)):
        x = L[i]
        if i < m:
            i = index
            m = x
        else:
            pass
    return (m,index)"""


def test_model(model_name: str):
    """
    Test the model by invoking it with a sample input.
    """
    try:
        llm = Ollama(model=model_name)
        print(ollama.show(model_name))
        print(
            llm.invoke(
                "Refactor this code to improve efficiency and readability:\n"
                + TEST_INPUT_CODE
            )
        )
    except Exception:
        print(f"Error testing model {model_name}.")


if __name__ == "__main__":
    if start_ollama_server():
        download_model("llama3")
        download_model("codellama")
        test_model("llama3")
        test_model("codellama")
        stop_ollama_server()
