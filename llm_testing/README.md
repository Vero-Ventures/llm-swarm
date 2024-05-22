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


