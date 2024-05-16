from pathlib import Path
import subprocess
import ollama
from langchain_community.llms import Ollama


def download_model(model_name: str, path: str | None = None):
    """
    Download the model to local machine. Defaults to `/.ollama/models`
    """

    if path:
        # FIXME: proper path handling
        Path(path).mkdir(parents=True, exist_ok=True)
        ollama_env = {"OLLAMA_MODELS": str(Path(path).resolve())}

    try:
        # start the ollama server - necessary for using the ollama package
        process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=ollama_env if path else None,
            text=True,
        )
        print("Ollama server started.")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Ollama is not installed. Please visit https://ollama.com/.")
        return

    current_models = [model["name"] for model in ollama.list().get("models")]
    if model_name not in current_models:
        try:
            print(f"Downloading model {model_name}...")
            ollama.pull(model_name)
        except ollama._types.ResponseError:
            print(f"Model {model_name} not found.")
            return

    process.terminate()

    # Test the model
    llm = Ollama(model=model_name)
    print(ollama.show(model_name))
    print(llm.invoke("The first man on the moon was ..."))


if __name__ == "__main__":
    # model_name = "llama3"
    model_name = "tinyllama"
    download_model(model_name)
