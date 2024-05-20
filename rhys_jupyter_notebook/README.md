## Run Jupyter Notebook
1. Right-click `rhys_jupyter_notebook` folder and select `Open in Integrated Terminal`

2. Run the following command

```bash
poetry run jupyter notebook
```
## Installation

1. Create a local directory. Clone the project repository into it.

2. Open a terminal at the directory location.

3. Install [Poetry](https://python-poetry.org), a package manager for Python. This will enable you to create a virtual environment and install the dependencies necessary for the project. This environment is self-contained and will not interfere with your system-wide Python installation.

```bash
pip install poetry
```

4. Create a `pyproject.toml` file. It _must_ be named `pyproject.toml` and _must_ be saved to the root of the project directory. This will contain all the dependencies required for the project.

5. Populate the `pyproject.toml` file with the following content and save it:

```toml
[tool.poetry]
name = "[insert-project-name]"
version = "0.1.0"
description = "[insert-project-description]"
authors = ["insert-your-name <insert-your-email>"]
readme = "README.md"

[tool.poetry.dependencies]
python = ">=3.11,<=3.13"
crewai = "^0.30.5"
langchain = "^0.1.20"
ollama = "^0.2.0"
jupyter = "^1.0.0"
ipykernel = "^6.29.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
6. To install the dependencies, open a terminal at the directory root and run the following command:

```bash
poetry install
```

7. Create a Jupyter kernal linked to the virtual environment.

```bash
poetry run python -m ipykernel install --user --name=INSERT-KERNAL NAME --display-name="INSERT-DISPLAY-NAME"
```

- REPLACE `--name` with a unique identifier for your kernel.
- REPLACE `--display-name` with the name you want to display in the Jupyter interface.

8. In the terminal, at the root of the directory, start the Jupyter server:

```bash
poetry run jupyter notebook
```
