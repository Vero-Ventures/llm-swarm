# Done by ChatGPT4

import random

def simulate_swiss_tournament():
    # Initialize teams
    teams = [{'wins': 0, 'losses': 0} for _ in range(16)]

    # Function to play a match between two teams
    def play_match(team1, team2):
        if random.choice([True, False]):
            teams[team1]['wins'] += 1
            teams[team2]['losses'] += 1
        else:
            teams[team2]['wins'] += 1
            teams[team1]['losses'] += 1

    # Continue rounds until conditions are met
    while any(team['wins'] < 3 and team['losses'] < 3 for team in teams):
        # Group teams by record
        record_groups = {}
        for i, team in enumerate(teams):
            record = (team['wins'], team['losses'])
            if record not in record_groups:
                record_groups[record] = []
            record_groups[record].append(i)

        # Match teams within the same record group
        for group in record_groups.values():
            random.shuffle(group)  # Shuffle to randomize pairings
            for i in range(0, len(group) - 1, 2):
                play_match(group[i], group[i+1])

    # Output the results
    results = {'promoted': [], 'eliminated': [], 'remaining': []}
    for i, team in enumerate(teams):
        if team['wins'] == 3:
            results['promoted'].append(i)
        elif team['losses'] == 3:
            results['eliminated'].append(i)
        else:
            results['remaining'].append(i)

    return results

# Run the simulation
result = simulate_swiss_tournament()
print("Promoted Teams:", result['promoted'])
print("Eliminated Teams:", result['eliminated'])
print("Remaining Teams:", result['remaining'])
