# Created by LLama3 via command line

import random

def swiss_tournament():
    # Initialize standings dictionary
    standings = {i: {'wins': 0, 'losses': 0} for i in range(16)}

    # All teams start with a 0-0 record and play a random opponent
    while True:
        teams_to_play = [i for i in range(16) if standings[i]['wins'] == 0 or standings[i]['losses'] == 0]
        random.shuffle(teams_to_play)

        for team1 in teams_to_play:
            for team2 in teams_to_play[teams_to_play.index(team1)+1:]:
                # Randomly decide who wins the match
                if random.random() < 0.5:
                    standings[team1]['wins'] += 1
                    standings[team2]['losses'] += 1
                else:
                    standings[team2]['wins'] += 1
                    standings[team1]['losses'] += 1

            # Check if a team has advanced to the Main Event or been eliminated
            for i in range(16):
                if standings[i]['wins'] >= 3:
                    print(f"Team {i} advances to the Main Event with a record of {standings[i]['wins']} wins and {standings[i]['losses']} losses.")
                elif standings[i]['losses'] >= 3:
                    print(f"Team {i} is eliminated from the tournament with a record of {standings[i]['wins']} wins and {standings[i]['losses']} losses.")

            # Check if all teams have advanced or been eliminated
            for team in range(16):
                if standings[team]['wins'] < 3 and standings[team]['losses'] < 3:
                    break
            else:
                print("All teams have either advanced to the Main Event or been eliminated.")
                return

# Example usage
swiss_tournament()
