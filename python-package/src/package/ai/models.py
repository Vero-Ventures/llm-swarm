import subprocess
import ollama
from langchain_community.llms import Ollama


def download_model(model_name: str):
    """
    Download the model to local machine (saves to `~/.ollama/models` by default).
    """
    try:
        # start the ollama server - necessary for using the ollama package
        process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
        )
        print("Ollama server started.")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Ollama is not installed. Please visit https://ollama.com/.")
        return

    locally_saved_models = [model["name"] for model in ollama.list().get("models")]
    if model_name not in locally_saved_models:
        try:
            print(f"Downloading model {model_name}...")
            ollama.pull(model_name)
        except ollama._types.ResponseError:
            print(f"Model {model_name} could not be retrieved.")
            return False

    # stop the ollama server
    process.terminate()
    print("Ollama server stopped.")

    # TODO: check if the model exists locally
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
