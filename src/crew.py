from crewai_agents import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class GameDeveloperCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config = self.agents_config['project_manager'],
            llm = self.groq_llm
        )

    @agent
    def senior_developer(self) -> Agent:
        return Agent(
            config = self.agents_config['senior_developer'],
            llm = self.groq_llm
        )

    @agent
    def senior_tester(self) -> Agent:
        return Agent(
            config = self.agents_config['senior_tester'],
            llm = self.groq_llm
        )

    @task
    def understand_project_requirements(self) -> Task:
        return Task(
            config = self.tasks_config['understand_project_requirements'],
            agent = self.project_manager()
        )

    @task
    def write_code(self) -> Task:
        return Task(
            config = self.tasks_config['write_code'],
            agent = self.senior_developer()
        )

    @task
    def test_code(self) -> Task:
        return Task(
            config = self.tasks_config['test_code'],
            agent = self.senior_tester()
        )

    @task
    def sign_off_on_project(self) -> Task:
        return Task(
            config = self.tasks_config['sign_off_on_project'],
            agent = self.project_manager()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )
