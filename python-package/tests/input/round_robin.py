import random

def round_robin_tournament(teams):
    # Initialize results dictionary
    results = {team: {"wins": 0, "losses": 0} for team in teams}

    # Iterate over all possible matchups
    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            team1 = teams[i]
            team2 = teams[j]

            # Print the game result (just for fun)
            print(f"{team1} vs {team2}: {team1} wins" if random.choice([True, False]) else f"{team1} vs {team2}: {team2} wins")

            # Update results
            if team1 == team2:
                continue  # can't win against themselves!
            if random.choice([True, False]):
                results[team1]["wins"] += 1
                results[team2]["losses"] += 1
            else:
                results[team2]["wins"] += 1
                results[team1]["losses"] += 1

    return results

teams = ["TeamA", "TeamB", "TeamC", "TeamD", "TeamE", "TeamF", "TeamG", "TeamH", "TeamI", "TeamJ"]
print(round_robin_tournament(teams))
