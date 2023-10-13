import random
import numpy as np
import json
from pathlib import Path


parent_dir = Path(__file__).parent.parent


def GetParameters(value, parameter_type, parameter):
    # Look up the parameters based on the specified value and parameter type
    for value_range, params in parameter[parameter_type].items():
        if value_range[0] <= value <= value_range[1]:
            return params


def PlayerNameGeneration():
    with open(parent_dir / 'data' / 'names.json') as json_file:
        data = json.load(json_file)

    firstNames = data['firstNames']
    lastNames = data['lastNames']

    # establish a list that contains all players in the league
    global totalPlayerList
    totalPlayerList = []
    
    # randomly generate names based off the name lists
    firstNameGeneration = random.choice(firstNames)
    lastNameGeneration = random.choice(lastNames)
        
    # create the full player name by combining both string values into one
    playerName = firstNameGeneration + " " + lastNameGeneration
        
    # add newly generated player name into botht the team's roster and the list of all players in the league
    totalPlayerList.append(playerName)
        
    # return roster list so this can later be assigned to the specific team it was created for
    return playerName


def PlayerWeightAndHeightGeneration():
    # Define height ranges and corresponding weight and wingspan statistics
    height_ranges = [(68, 72, 170, 210, 190, 8, 68, 72),
                    (73, 78, 185, 235, 210, 10, 73, 78),
                    (79, 84, 215, 275, 245, 12, 79, 84),
                    (85, 90, 250, 330, 285, 15, 85, 90)]

    # Generate a random height within the specified range
    minHeight, maxHeight, minWeight, maxWeight, meanWeight, stdDevWeight, minWingspan, maxWingspan = random.choice(height_ranges)
    heightInches = np.random.randint(minHeight, maxHeight + 1)

    # Calculate feet and inches
    feet = heightInches // 12
    inches = heightInches % 12
    height = f"{feet}'{inches}"

    # Generate a random weight within the specified range
    weight = np.random.randint(minWeight, maxWeight + 1)

    # Generate a random wingspan within the specified range
    wingspan = np.random.randint(minWingspan, maxWingspan + 1)

    return [height, weight, wingspan]


def StrengthGeneration(height, weight):
    minStrength = 25
    maxStrength = 100

    height_weight_ranges = {
        (68, 72, 170, 190): (45, 10),
        (68, 72, 191, 210): (75, 10),
        (73, 78, 185, 200): (50, 10),
        (73, 78, 201, 215): (70, 10),
        (73, 78, 216, 235): (80, 10),
        (79, 84, 215, 235): (60, 10),
        (79, 84, 236, 255): (75, 10),
        (79, 84, 256, 275): (85, 8),
        (85, 90, 250, 275): (70, 10),
        (85, 90, 276, 295): (80, 10),
        (85, 90, 296, 330): (90, 5)
    }

    strength_mean, strength_sd = height_weight_ranges.get((height, weight), (None, None))

    if strength_mean is not None:
        strength = np.random.normal(strength_mean, strength_sd)
        strength = np.round(strength).astype(int)
    else:
        strength = np.random.randint(minStrength, maxStrength + 1)

    # Ensure skill falls within the specified min and max limits
    strength = max(minStrength, min(maxStrength, strength))

    return strength


def VerticalGeneration(height, weight):
    minSkill = 0
    maxSkill = 100

    # Define skill parameters based on height and weight ranges
    skillParameters = {
        "heightRange": {
            (68, 72): {"mean": 80, "sd": 5},
            (73, 78): {"mean": 85, "sd": 6},
            (79, 84): {"mean": 75, "sd": 8},
            (85, 90): {"mean": 65, "sd": 10},
        },
        "weightRange": {
            (170, 190): {"mean": 85, "sd": 5},
            (191, 210): {"mean": 85, "sd": 6},
            (211, 230): {"mean": 80, "sd": 8},
            (231, 250): {"mean": 70, "sd": 8},
            (251, 270): {"mean": 65, "sd": 8},
            (271, 300): {"mean": 60, "sd": 8},
            (301, 330): {"mean": 50, "sd": 10},
        }
    }

    # Helper function to get parameters from the skillParameters dictionary
    def GetParameters(value, category, parameters):
        for range_, params in parameters[category].items():
            if range_[0] <= value <= range_[1]:
                return params

    heightParameters = GetParameters(height, "heightRange", skillParameters)
    weightParameters = GetParameters(weight, "weightRange", skillParameters)

    # Calculate combined skill based on height and weight parameters
    combinedMean = (heightParameters["mean"] + weightParameters["mean"]) / 2
    combinedSD = (heightParameters["sd"] + weightParameters["sd"]) / 2

    # Generate a random skill value within the specified range
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)

    # Ensure skill falls within the specified min and max limits
    skill = max(minSkill, min(maxSkill, skill))

    return skill


def FootworkGeneration(height, weight):
    minSkill = 0
    maxSkill = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 6'0
            (68,72): {"mean": 85, "sd": 5},
            # height: 6'1 - 6'6
            (73,78): {"mean": 75, "sd": 7},
            # height: 6'7 - 7'0
            (79,84): {"mean": 80, "sd": 7},
            # height: 7'1 - 7'6
            (85,90): {"mean": 65, "sd": 10},
        },
        "weightRange": {
            (170, 190): {"mean": 80, "sd": 5},
            (191, 210): {"mean": 75, "sd": 5},
            (211, 230): {"mean": 70, "sd": 8},
            (231, 270): {"mean": 80, "sd": 5},
            (271, 300): {"mean": 65, "sd": 5},
            (301, 330): {"mean": 60, "sd": 10},
        }
    } 
    
    heightParameters = GetParameters(height, "heightRange", skillParameters)
    weightParameters = GetParameters(weight, "weightRange", skillParameters)
    
    combinedMean = heightParameters["mean"] + weightParameters["mean"]
    combinedMean = combinedMean / 2
    combinedSD = heightParameters["sd"] + weightParameters["sd"]
    combinedSD = combinedSD / 2
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxSkill:
        skill = random.randint(95, 100)
    if skill < minSkill:
        skill = random.randint(0, 15)
        
    return skill


def SpeedGeneration(height, weight):
    minSkill = 0
    maxSkill = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 6'0
            (68,72): {"mean": 90, "sd": 5},
            # height: 6'1 - 6'6
            (73,78): {"mean": 80, "sd": 6},
            # height: 6'7 - 7'0
            (79,84): {"mean": 70, "sd": 7},
            # height: 7'1 - 7'6
            (85,90): {"mean": 55, "sd": 10},
        },
        "weightRange": {
            (170, 190): {"mean": 90, "sd": 5},
            (191, 210): {"mean": 85, "sd": 5},
            (211, 230): {"mean": 80, "sd": 5},
            (231, 250): {"mean": 70, "sd": 6},
            (251, 270): {"mean": 68, "sd": 7},
            (271, 300): {"mean": 65, "sd": 8},
            (301, 330): {"mean": 55, "sd": 10},
        }
    } 
    
    heightParameters = GetParameters(height, "heightRange", skillParameters)
    weightParameters = GetParameters(weight, "weightRange", skillParameters)
    
    combinedMean = heightParameters["mean"] + weightParameters["mean"]
    combinedMean = combinedMean / 2
    combinedSD = heightParameters["sd"] + weightParameters["sd"]
    combinedSD = combinedSD / 2
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxSkill:
        skill = random.randint(95, 100)
    if skill < minSkill:
        skill = random.randint(0, 15)
        
    return skill
    
    
def StaminaGeneration(height, weight):
    minSkill = 0
    maxSkill = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 6'0
            (68,72): {"mean": 90, "sd": 5},
            # height: 6'1 - 6'6
            (73,78): {"mean": 85, "sd": 6},
            # height: 6'7 - 7'0
            (79,84): {"mean": 80, "sd": 7},
            # height: 7'1 - 7'6
            (85,90): {"mean": 70, "sd": 10},
        },
        "weightRange": {
            (170, 190): {"mean": 90, "sd": 5},
            (191, 210): {"mean": 85, "sd": 5},
            (211, 230): {"mean": 82, "sd": 5},
            (231, 250): {"mean": 80, "sd": 6},
            (251, 270): {"mean": 78, "sd": 7},
            (271, 300): {"mean": 75, "sd": 7},
            (301, 330): {"mean": 60, "sd": 8},
        }
    } 
    
    heightParameters = GetParameters(height, "heightRange", skillParameters)
    weightParameters = GetParameters(weight, "weightRange", skillParameters)
    
    combinedMean = heightParameters["mean"] + weightParameters["mean"]
    combinedMean = combinedMean / 2
    combinedSD = heightParameters["sd"] + weightParameters["sd"]
    combinedSD = combinedSD / 2
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxSkill:
        skill = random.randint(95, 100)
    if skill < minSkill:
        skill = random.randint(0, 15)
        
    return skill
