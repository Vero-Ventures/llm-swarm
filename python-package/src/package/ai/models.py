import subprocess
import time
import ollama
from langchain_community.llms import Ollama


def get_local_models():
    """
    Get the list of locally saved models.
    """
    return [model["name"] for model in ollama.list().get("models")]


def download_model(model_name: str):
    """
    Download the model to local machine (saves to `~/.ollama/models` by default).
    """
    try:
        # Start the ollama server (necessary for using the ollama package)
        # and let continue running in the background
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            # shell=True,
        )
        # give the server some time to start
        time.sleep(3)

        print("Ollama server started.")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Ollama is not installed. Please visit https://ollama.com/.")
        return

    print("Checking if model exists locally...")
    if model_name not in get_local_models():
        try:
            print(f"Downloading model {model_name}...")
            ollama.pull(model_name)
        except ollama._types.ResponseError:
            print(f"Model {model_name} could not be retrieved.")
            return False
    else:
        print(f"Model {model_name} already exists locally.")

    return True


def test_model(model_name: str):
    llm = Ollama(model=model_name)
    print(ollama.show(model_name))
    print(llm.invoke("The first man on the moon was ..."))


if __name__ == "__main__":
    # model_name = "llama3"
    model_name = "tinyllama"
    download_model(model_name)
    test_model(model_name)
