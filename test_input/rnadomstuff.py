import random
import itertools
import pickle

class Team:
    def __init__(self):
        self.skill = [random.randint(1, 10000) for _ in range(20)]
        self.wins = 0
        self.losses = 0

    def play(self):
        index = random.randint(0, len(self.skill) - 1)
        return (self.skill[index], index)

    def learn_rem(self, index):
        self.skill.pop(index)
        self.skill.sort(reverse=True)
        if len(self.skill) < 3:
            self.skill.append(random.randint(1, 10000))
            self.skill.append(random.randint(1, 10000))



    def learn_add(self, index):
        self.skill.append(self.skill[index])
        
        self.skill.sort(reverse=True)
        #self.skill.pop(0)
        self.skill.append(random.randint(1, 10000))

    def print_skill(self):
        print(self.skill)
        count = 0
        for item in self.skill:
            count += item
        print(f"average: {count / len(self.skill) / 100}")
        

class League:
    def __init__(self):
        team_names = ["Quantum", "Neon", "Shadows", "Cosmos", "Thunder", "Voltage", "Eclipse", "Vortex", "Sapphire", "Ironside", "Celestial", "Galactic", "Inferno", "Blizzard", "Fireborne", "Mystic"]
        self.teams = [Team() for _ in range(len(team_names))]
        self.team_dict = {name: team for name, team in zip(team_names, self.teams)}

    def update_teams(self):
        print("Updating teams")
        for team in self.teams:
            team.replace_random_player()
            team.sort_players()
            team.wins = 0
            team.losses = 0

    def match(self, team1_name, team2_name):
        team1 = self.team_dict[team1_name]
        team2 = self.team_dict[team2_name]
        team1_points = 0
        team2_points = 0
        for _ in range(5):
            skill_1, index_1 = team1.play()
            skill_2, index_2 = team2.play()
            if skill_1 >= skill_2:
                team1_points += 1
                team1.learn_add(index_1)
                team2.learn_rem(index_2)
            else:
                team2_points += 1
                team2.learn_add(index_2)
                team1.learn_rem(index_1)

        if team1_points > team2_points:
            print(f"{team1_name} wins the match against {team2_name} {team1_points}-{team2_points}.")
            team1.wins += 1
            team2.losses += 1
            return team1_name, team2_name
        else:
            print(f"{team2_name} wins the match against {team1_name} {team2_points}-{team1_points}.")
            team1.losses += 1
            team2.wins += 1
            return team2_name, team1_name


    def round_robin(self):
        """Generate round robin matches"""

        # Create a list of matches, excluding self-play
        matchups = list(itertools.combinations(self.team_dict, 2))
        random.shuffle(matchups)
        for match in matchups:
            self.match(*match)

    def print_all_teams(self):
        for name, team in self.team_dict.items():
                print(name)
                team.print_skill()
                print()
            

def save_league_state(league):
        """
        Save the state of the league to a file using pickle.

        Args:
        league (League): The league object to be saved.
        filename (str): The name of the file where the league state will be saved.
        """
        with open("save", 'wb') as f:
            pickle.dump(league, f)

def load_league_state():
        """
        Load the state of the league from a file using pickle.

        Args:
        filename (str): The name of the file from which to load the league state.

        Returns:
        League: The loaded league object.
        """
        with open("save", 'rb') as f:
            return pickle.load(f)




def main():
    new = input("new file? (y/N)")
    if new == "y":
        print("creating new save")
        league = League()
        save_league_state(league)
    else:
        try: 
            league = load_league_state()
            print("loaded")
        except: 
            league = League()
            print("new save required")
            save_league_state(league)
    while True:
        
        team1 = input("team1: ")
        if team1 == "p":
            league.print_all_teams()
        team2 = input("team2: ")
        if team2 == "r":
            league.round_robin()
            sorted_teams = sorted(league.team_dict.items(), key=lambda item: item[1].wins, reverse=True)
            # Display results
            print("\n\nResults\n")
            for name, team in sorted_teams:
                print(f"{name}: {team.wins} Wins, {team.losses} Losses")
        try: 
            league.match(team1, team2)
            save_league_state(league)


        except: print("misinput")
        

if __name__ == "__main__":
    main()

        
        