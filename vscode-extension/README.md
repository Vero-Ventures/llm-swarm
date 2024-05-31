# Using CrewsControl

## Initialize Ollama

This extension relies on [Ollama](https://ollama.com/). After installing it, you will need to pull the requisite LLMs to your machine. You can do this by running the following commands in the terminal:

> **Note:** These models together will require about 8.5 GB of disk space, and may take a few minutes to download.

```bash
ollama pull llama3
ollama pull codellama
```

Then start the Ollama server by running the app, or by entering the following command in the terminal:

```bash
ollama serve
```

## Refactoring Code

### Improve Selection

To refactor a portion of code, select the code you want to refactor, right-click, and select `CrewsControl: Improve Selection`.

You can also access this command via the VS Code Command Palette by pressing `Ctrl+Shift+P` and typing `CrewsControl: Improve Selection`.

### Improve File

To refactor an entire file, right-click in the editor and select `CrewsControl: Improve File`.

You can also access this command via the VS Code Command Palette by pressing `Ctrl+Shift+P` and typing `CrewsControl: Improve File`.
