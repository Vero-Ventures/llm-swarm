from dotenv import load_dotenv

load_dotenv()

from crewai import Crew

from tasks import GameTasks
from agents import GameAgents

tasks = GameTasks()
agents = GameAgents()

print("## Welcome to the Game Crew")
print("-------------------------------")
game = input("What is the game you would like to build? What will be the mechanics?\n")

# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
code_game = tasks.code_task(senior_engineer_agent, game)
review_game = tasks.review_task(qa_engineer_agent, game)
approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)

# Create Crew responsible for Copy
crew = Crew(
    agents=[senior_engineer_agent, qa_engineer_agent, chief_qa_engineer_agent],
    tasks=[code_game, review_game, approve_game],
    verbose=True,
)

game = crew.kickoff()


# Print results
print("\n\n########################")
print("## Completed Game")
print("########################\n")
print("final code for the game going to file game.py")

# strip the markdown formatting from the start "```python" if it exists
if game.startswith("```python"):
    game = game[9:]

# strip the markdown formatting from the end ``` if it exists, and any text after it,
# in case the llm added extra text
if "```" in game:
    game = game[: game.index("```")]

# Save the game code to a file
with open("game.py", "w") as f:
    f.write(game)
    print("\n\nGame code saved to game.py")
