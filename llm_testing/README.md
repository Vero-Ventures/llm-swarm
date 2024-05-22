# Research Project

## Description
In this research document, we briefly explore the capabilities of AI agents, powered by a local large language model (LLM), to improve small snippets of code. Specifically, we explore AI agent swarms, which are groups of AI agents that work together to achieve a common goal.

For our testing, we use a popular local LLM, [**Llama3**](https://github.com/meta-llama/llama3), the eight-billion parameter version, and the [**CrewAI**](https://www.crewai.com) framework, one of the most popular open-source frameworks for building AI agents.

### What is an AI Agent?
Agents are entities, programmed by humans and powered by LLMs, that have a defined role and perform tasks related to that role. You may think of an agent as an employee who is responsible for a specific task or function within an organization.

### What are Agent Swarms?
Agent Swarms are groups of AI agents that work together to achieve a common goal. They are composed of multiple agents, each with its own unique capabilities and strengths, and they work together to solve complex problems. You may think of an agent swarm similar to an organization, where each agent has different a different role and responsibility, and together they work to achieve a common goal.

## Objectives

## Tools & Technologies

## Methodology

## Challenges

## Findings

## Recommendations

---

# Installation

1. **Clone the repository**: Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/Vero-Ventures/llm-swarm.git
cd llm-swarm
```

2. **Install Poetry**: Poetry is a package manager for Python that allows you to manage dependencies and run Python code in a virtual environment. To install Poetry, follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

3. **Install Project Dependencies**: Open a terminal at the root of the repository and run the following command to install the project dependencies:

```bash
poetry install
```

4.



1. Clone the repository to the directory of your choice

2. Project dependencies are managed using the Poetry package manager. Install Poetry by following the instructions on the [website](https://python-poetry.org/).

3. Navigate to the project directory, open a terminal, and run the following command to install the project dependencies:

```bash
poetry install
```

4. Next, add Jupyter Notebook to the project dependencies by running the following command:

```bash
poetry add jupyter
```

5. Open a Poetry shell, which allows you to run commands in the virtual environment and access the project's dependencies. To open a Poetry shell, run the following command:

```bash
poetry shell
```

6. You must install the kernel for the Jupyter Notebook. This kernel ties the notebook to the virtual environment and allows you to run Python code within the notebook.

```bash
python -m ipykernel install --user --name llm-swarm-kernel --display-name "LLM Swarm"
```
- The `--name` flag is a unique name for the kernel, which is used by Jupyter to identify the kernel.
- The `--display-name` flag is a human-readable name for the kernel, which is displayed in the Jupyter interface.

7. Start the Jupyter Notebook server by running the following command:

```bash
jupyter notebook
```

This should automatically open a new tab in your web browser, where you can access the Jupyter Notebook interface.








We used a popular local LLM, **Llama3**, the eight-billion parameter version. We downloaded and managed these LLMs using [**Ollama**](https://ollama.com), an open-source platform for running LLMs locally.

For our testing, we created a custom Llama3 model with a set seed. A seed means that the same input will produce the same output, allowing us to more accurately test a model.

(Seeding, in practice, does not produce exactly the same output given a certain input; this is due to several reasons, including stochastic sampling, model parameter size, and so on.)

Custom models are stored in the same place, locally, as the default model.

### MacOS

`/Users/[username]/.ollama/models/manifests/registry.ollama.ai/library`

### Windows

`C:\Users\[username]\.ollama\manifests\registry.ollama.ai\library\`

### Linux

`/var/lib/ollama/.ollama/models/manifests/registry.ollama.ai/library`

If you want to initialize a custom model, simply reference the name of the model as you would the default model:

```Python
llm = Ollama(model="[custom_model_name")
```

This will automatically look in the same directory as the default model.


## Creating a Custom-Seeded Model

1. Create a new file
2. Name the file. Do NOT include a file format.
3. Open the file in a text editor and include the following:

```bash
# Set the base model
FROM llama3:8b

# Set custom parameters
PARAMETER temperature 0.7  # Optional
PARAMETER seed 42
```

4. Save the file.
5. Open a terminal and write the following command:

```bash
ollama create [model_name] -f /path/to/my_custom_model
```

6. To check if the model was successfully created, run `ollama list`; you should see `[model_name]` in the list
