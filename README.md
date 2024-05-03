## **Project Description**

This project proposes an ambitious framework, powered by AI, to revolutionize software development. The framework will utilize Large Language Model (LLM) driven multi-agent swarms to construct software applications.

**Initial Scope:**

- The LLM swarm will initially focus on building software using Python and TypeScript.

## Running the Script

You can use any LLM you wish, but GPT4 is recommended. To run the script, follow these steps:

- **Configure Environment**: Copy `.env.example`, rename to `.env`, and add the appropriate values to the environment variables
- **Install Dependencies**: Run `poetry install --no-root`
- **Execute the Script**: Run `poetry run python main.py` _OR_ enter the virtual environment with `poetry shell` and then run `python main.py`

## Details & Explanation

**Key Components**:

- `./main.py` - Main script that gets input code, sets up AI crew, passed code to crew, and produces output code.
- `./agents.py` - Defines the SWE agents in the crew.
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

- Devin: https://www.cognition-labs.com/introducing-devin
- AutoGen: https://github.com/microsoft/autogen
- CrewAI: https://github.com/joaomdmoura/crewai
- ACE Framework: https://github.com/daveshap/ACE_Framework
- Hierarchical Autonomous Agent Swarm (HAAS): https://github.com/daveshap/OpenAI_Agent_Swarm

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
