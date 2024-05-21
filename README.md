# AI Agent Swarm for Code Improvement

## **Project Description**

This project aims to build code improvement software that utlizes an AI agent swarm using remote OR locally hosted models. There are two main components to this project:

- A Python package that can be used as a CLI to perform AI tasks.
- A VSCode extension that uses the package to perform tasks based on inputs derived from the IDE.

## Setting up the Project

### Python package management with `poetry`

1. Install the `poetry` package manager - find instructions [here](https://python-poetry.org/docs/#installing-with-the-official-installer).
2. In terminal navigate to `/python-package` and install the required dependencies by running:

```shell
poetry install --no-root
```

<!-- markdownlint-disable MD029 -->

3. Install the `pre-commit` hooks by running:

```shell
poetry run pre-commit install
```

### Environment Variables

Make a copy of `.env.example`, rename it to `.env`, and add the appropriate values for the environment variables.

### Node.js package management with `npm`

In terminal navigate to `/vscode-extension` and install the required npm packages by running:

```shell
npm install --save-dev eslint@8.57.0 globals prettier @typescript-eslint/parser @typescript-eslint/eslint-plugin typescript
```

## Running the Script

The main script can be run as a CLI tool from within the `/python-package`:

```shell
poetry run cli  # use -h for help
```

Alternatively, enter the virtual environment with `poetry shell` and then run `python main.py`, or simply run `poetry run python main.py`.

There is also a bash script in the root folder that may be freely altered for testing purposes. Run it with:

```shell
./test.sh
```

## Details & Explanation

**Key Components**:

- `./main.py` - Main script that gets input code, sets up AI crew, passed code to crew, and produces output code.
- `./agents.py` - Defines the SWE AI agents in the crew.
- `./tasks.py` - Defines the tasks (i.e. prompts) carried out by the agents.

**Framework Capabilities:**

- **Autonomous Tasks:** Perform a wide range of software engineering activities including:
  - Learning new technologies
  - Building and deploying applications
  - Identifying and fixing bugs
  - Training and fine-tuning AI models
- **Collaborative Environment:** Integrate common developer tools like a shell, code editor, and browser within a sandboxed environment. This allows both AI swarms and human engineers to work collaboratively on projects.
- **Transparent Operations:** The framework will showcase its progress in real-time, allowing human intervention with additional prompts to guide the system towards desired outcomes.

**Long-Term Goal:**

- Formalize the software development process as AI-compatible instructions.

**Similar Projects:**

- Devin: <https://www.cognition-labs.com/introducing-devin>
- AutoGen: <https://github.com/microsoft/autogen>
- CrewAI: <https://github.com/joaomdmoura/crewai>
- ACE Framework: <https://github.com/daveshap/ACE_Framework>
- Hierarchical Autonomous Agent Swarm (HAAS): <https://github.com/daveshap/OpenAI_Agent_Swarm>

## **Programming Language(s)**

- Primary: Python (utilizing AI and LLM libraries)

## **Hardware/Software Requirements**

- **Programming Language:** Python
- **Developer Tools:**
  - Integrated Development Environment (IDE)
  - Code Interpreter
  - Web Browser
- **DevOps Tools:** Tools for continuous integration and deployment (CI/CD) processes
- **Computational Resources:** Local server with high computational power for AI operations and software development tasks.

## **Current Work/Arrangement**

Software development is traditionally a manual process with stages ranging from conception to deployment. Tasks like debugging, deployment, and learning new technologies are handled by human developers. This project aims to leverage Python AI libraries to build a framework that automates and optimizes these tasks, enhancing development efficiency and creativity.
