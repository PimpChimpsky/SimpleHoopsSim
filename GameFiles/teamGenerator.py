import random
import json
from pathlib import Path


parent_dir = Path(__file__).parent.parent

def TeamGeneration():
    with open(parent_dir / 'data' / 'cityteam.json') as json_file:
        data = json.load(json_file)

    cityNames = data['cityNames']
    teamNames = data['teamNames']

    # establish a total team list that can be called on all throughout the code
    global totalTeamList
    totalTeamList = []
    
    # randomly generate city and team names from the lists
    cityGeneration = random.choice(cityNames)
    teamNameGeneration = random.choice(teamNames)
    
    # remove the generated city and team names to avoid repeating names
    cityNames.remove(cityGeneration)
    teamNames.remove(teamNameGeneration)
    
    # establish team variable and combine the string values of the city and team name
    global team
    team = cityGeneration + " " + teamNameGeneration
        
    # add newly generated team to total team list
    totalTeamList.append(team)

    print(team)
    return team
