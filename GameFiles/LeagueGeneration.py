# This file is called upon to generate a whole league

# IMPORTS
import random
import pandas as pd
import numpy as np

import OffenseGeneration
from OffenseGeneration import OffenseGeneration

# LISTS

# create lists for all of the randomized elements that are generated later
firstNames = ["James", 'Robert', 'John', "Michael", "David", "William", "Richard", "Joseph", "Thomas", "Chris", "Anthony", "Paul", "Kenneth", "Kevin", "George", "Jason", "Ryan", "Bruce",
              'Tyler', 'Jacob', 'Austin', 'Jordan', 'Brandon', 'Joshua', 'Andrew', 'Rafael', 'Peyton', 'Alex', 'Coby', 'Kobe', 'Bryan', 'Rocky', 'Shawn', 'Sean', 'Cody', 'Robby', 'Stephen',
              'Steven', 'Steve', 'Will', 'Phil', 'Nolan', 'Charles', 'Chris', 'Derick', 'Conor', 'Mason', 'Shaun', 'Emmitt', 'Tom', 'Bill', 'Cameron', 'Derek', 'Hugo', 'Daniel', 'Henry',
              'Jayden', 'Noah', 'Samuel', 'Mateo', 'Jack', 'Owen', 'Ethan', 'Levi', 'Ace', 'Van', 'Xavier', 'Dominic', 'Damian', 'Donovan', 'Jamal', 'James', 'Jimmy', 'Bobby', 'Jaylen',
              'Jalen', 'Kenyon', 'Nikola', 'Jeremiah', 'Jermaine', 'Kingston', 'Jonah', 'Chase', 'Jerry', 'Stephen', 'Boban', 'Juancho', 'Jose', 'Enrique', 'Ivan', 'Max']

lastNames = ["Anthony", "Paul", "Wang", "Smith", "Ivanov", "Mohammad", "Gonzalez", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Wilson", "Anderson", "Thomas", 
             "Jackson", "Scott", "Santagato", 'Brady', 'Sanders', 'Granger', 'Carter', 'Rezonov', 'Hernandez', 'Lopez', 'Gonzales', 'Jordan', 'Moore', 'Wright', 'Martinez', 'Thompson',
             'Harris', 'White', 'Sanchez', 'Clark', 'Lee', 'Hill', 'Scott', 'King', 'Walker', 'Torres', 'Flores', 'Green', 'Porter', 'Martin', 'Baker', 'Evans', 'Mitchell', 'Fox', 
             'Turner', 'Reyes', 'Collins', 'Stewart', 'Morris', 'Morales', 'Murphy', 'Cruz', 'Parker', 'Rogers', 'Reed', 'Howard', 'Cox', 'Bailey', 'Peterson', 'Morgan', 'Cooper',
             'Richardson', 'Wood', 'Bennet', 'Gray', 'Brooks', 'Richardson', 'James', 'Watson', 'Price', 'Sanders', 'Patel', 'Long', 'Foster', 'Griffin', 'Young', 'Fisher', 'Jones',
             'Little', 'Meyer', 'Weber', "O'Neal", 'Russo', 'Garcia', 'Silva', 'Novak', 'Miller', 'Ivanov', 'Murphy', 'Schmit', 'Wiggins']

cityNames = ["Mexico City", "New York City", "Los Angeles", "Toronto", "Chicago", "Houston", "Montreal", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Austin", 
             "Jacksonville", "San Jose", "Fort Worth", "Columbus", "Charlotte", "Indianapolis", "San Francisco", "Seattle", "Denver", "Oklahoma City", "Nashville", "El Paso", 
             "Washington D.C.", "Las Vegas", "Boston", "Portland", "Louisville", "Memphis", "Detroit", "Baltimore", "Milwaukee", "Albuquerque", "Sacramento", "Atlanta", "New Orleans"]
teamNames = ["Aristocrats", "Mermaids", "Forces", "Sharks", "Owls", "Vampires", "Giants", "Foxes", "Beavers", "Pioneers", "Mustangs", "Leopards", "Huskies", "Bandits", "Bulldogs", "Angels", 
             "Dreamers", "Cougars", "Lions", "Tigers", "Dolphins", "Wolves", "Iguanas", "Blobfishes", "Cannibals", "Skin Walkers", "Cryptids", "Moth Men", "Vultures"]


skills = ["offense", "defense", "playmaking", "rebounding", "dribbling", "iq", "mentality", "physicals"]

offense = ["3pt scoring", "midrange", "freethrow", "fade-away", "layups", "floater", "dunks", "post scoring", "flashy scoring"]
defense = ["perimeter defense", "post defense", "steals", "blocks", "lateral quickness"]
playmaking = ["pass accuracy", "pass iq", "alley-oop pass", "flashy passing"]
rebounding = ["defensive rebounding", "offensive rebounding"]
dribbling = ["ball control", "dribble quickness", "flashy dribbling"]
iq = ["court vision", "defensive iq", "coach", "off-ball movement"]
mentality = ["clutchness", "mentor", "rage"]
physicals =["height", "weight", "strength", "vertical", "footwork", "speed", "stamina"]



# FUNCTIONS     
 
def GetParameters(value, parameter_type, parameter):
    # Look up the parameters based on the specified value and parameter type
    for value_range, params in parameter[parameter_type].items():
        if value_range[0] <= value <= value_range[1]:
            return params
 
# TEAMS
# function called upon to create team names
def TeamGeneration():
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
    
    
    

# PLAYER
# function called on to generate player names
def PlayerNameGeneration():
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
    # set max and min height
    minHeight = 68
    maxHeight = 90
    
    # generate height
    mean = 79
    stdDev = 3
    heightInches = np.random.normal(mean, stdDev)
    heightInches = np.round(heightInches).astype(int)
    
    # make sure all heights fit within range
    if heightInches < minHeight:
        heightInches = random.randint(88, 90)
    elif heightInches > maxHeight:
        heightInches = random.randint(68, 72)
    
    # convert height to feet and inches
    feet = heightInches // 12
    inches = heightInches % 12
    
    # make height variable with these values
    feetStr = str(feet)
    inchesStr = str(inches)
    height = feetStr + "'" + inchesStr
    
    # weight generation
    # height: 5'8 - 6'0
    if 68 <= heightInches <= 72:
        
        minWeight = 170
        maxWeight =  210
        
        meanWeight = 190
        stdDevWeight = 8
        
        weight = np.random.normal(meanWeight,stdDevWeight)
        weight = np.round(weight).astype(int)
        
        if weight < minWeight:
            weight = random.randint(170, 175)
        elif weight > maxWeight:
            weight = random.randint(205, 210)
            
    # height: 6'1 - 6'6
    elif 73 <= heightInches <= 78:
       
        minWeight = 185
        maxWeight =  235
        
        meanWeight = 210
        stdDevWeight = 10
        
        weight = np.random.normal(meanWeight,stdDevWeight)
        weight = np.round(weight).astype(int)
        
        if weight < minWeight:
            weight = random.randint(185, 192)
        elif weight > maxWeight:
            weight = random.randint(227, 235)
            
    # height: 6'7 - 7'0
    elif 79 <= heightInches <= 84:
        
        minWeight = 215
        maxWeight =  275
        
        meanWeight = 245
        stdDevWeight = 12
        
        weight = np.random.normal(meanWeight,stdDevWeight)
        weight = np.round(weight).astype(int)
        
        if weight < minWeight:
            weight = random.randint(215, 225)
        elif weight > maxWeight:
            weight = random.randint(265, 275)
            
    # height: 7'1 - 7'6
    elif 85 <= heightInches <= 90:
        
        minWeight = 250
        maxWeight =  330
        
        meanWeight = 285
        stdDevWeight = 15
        
        weight = np.random.normal(meanWeight,stdDevWeight)
        weight = np.round(weight).astype(int)
        
        if weight < minWeight:
            weight = random.randint(250, 260)
        elif weight > maxWeight:
            weight = random.randint(315, 330)
            
        
        
    # wingspan generation
    # height: 5'8 - 5'9
    if heightInches == 68 or heightInches == 69:
        # wingspan: 5'5 - 6'4
        minWingspan = 65
        maxWingspan = 76
        
        meanWingspan = 72
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(65,67)
        elif wingspan > maxWingspan:
            wingspan = random.randint(75,76)
        
    # height: 5'10 - 5'11
    elif heightInches == 70 or heightInches == 71:
        # wingspan: 5'7 - 6'6
        minWingspan = 67
        maxWingspan = 78
        
        meanWingspan = 74
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(67,69)
        elif wingspan > maxWingspan:
            wingspan = random.randint(77,78)
        
    # height: 6'0 - 6'1
    elif heightInches == 72 or heightInches == 73:
        # wingspan: 5'9 - 6'8
        minWingspan = 69
        maxWingspan = 80
        
        meanWingspan = 76
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(69,71)
        elif wingspan > maxWingspan:
            wingspan = random.randint(79,80)
        
    # height: 6'2 - 6'3
    elif heightInches == 74 or heightInches == 75:
        # wingspan: 5'11 - 6'10
        minWingspan = 71
        maxWingspan = 82
        
        meanWingspan = 78
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(71,73)
        elif wingspan > maxWingspan:
            wingspan = random.randint(81,82)
        
    # height: 6'4 - 6'5
    elif heightInches == 76 or heightInches == 77:
        # wingspan: 6'1 - 7'0
        minWingspan = 73
        maxWingspan = 84
        
        meanWingspan = 80
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(73,75)
        elif wingspan > maxWingspan:
            wingspan = random.randint(83,84)
        
    # height: 6'6 - 6'7
    elif heightInches == 78 or heightInches == 79:
        # wingspan: 6'3 - 7'2
        minWingspan = 75
        maxWingspan = 86
        
        meanWingspan = 82
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(75,77)
        elif wingspan > maxWingspan:
            wingspan = random.randint(85,86)
        
    # height: 6'8 - 6'9
    elif heightInches == 80 or heightInches == 81:
        # wingspan: 6'5 - 7'4
        minWingspan = 77
        maxWingspan = 88
        
        meanWingspan = 84
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(77,79)
        elif wingspan > maxWingspan:
            wingspan = random.randint(83,84)
        
    # height: 6'10 - 6'11
    elif heightInches == 82 or heightInches == 83:
        # wingspan: 6'7 - 7'6
        minWingspan = 79
        maxWingspan = 90
        
        meanWingspan = 86
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(79,81)
        elif wingspan > maxWingspan:
            wingspan = random.randint(89,90)
        
    # height: 7'0 - 7'1
    elif heightInches == 84 or heightInches == 85:
        # wingspan: 6'9 - 7'8
        minWingspan = 81
        maxWingspan = 92
        
        meanWingspan = 88
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(81,83)
        elif wingspan > maxWingspan:
            wingspan = random.randint(91,92)
        
    # height: 7'2 - 7'3
    elif heightInches == 86 or heightInches == 87:
        # wingspan: 6'11 - 7'10
        minWingspan = 83
        maxWingspan = 94
        
        meanWingspan = 90
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(83,85)
        elif wingspan > maxWingspan:
            wingspan = random.randint(89,90)
        
    # height: 7'4 - 7'6
    elif heightInches == 88 or heightInches == 89 or heightInches == 90:
        # wingspan: 7'11 - 8'0
        minWingspan = 85
        maxWingspan = 97
        
        meanWingspan = 92
        stdDevWingspan = 2
        
        wingspan = np.random.normal(meanWingspan, stdDevWingspan)
        wingspan = np.round(wingspan).astype(int)
        
        if wingspan < minWingspan:
            wingspan = random.randint(85,87)
        elif wingspan > maxWingspan:
            wingspan = random.randint(95,97)
        
    # wingspanDifference = wingspan - heightInches
        
    combined = []
    combined.append(height)
    combined.append(weight)
    combined.append(wingspan)
    # combined.append(wingspanDifference)
    return combined
    
    
    
def StrengthGeneration(height, weight):
    minSkill = 0
    maxSkill = 100
    
    # if statement since weight to height ratio matters as opposed to just weight and height
    # height: 5'8 - 6'0
    if 68 <= height <= 72:
        if 170 <= weight <= 190:
            mean = 45
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
        elif 191 <= weight <= 210:
            mean = 75
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
    # height: 6'1 - 6'6
    elif 73 <= height <= 78:
        if 185 <= weight <= 200:
            mean = 50
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
        elif 201 <= weight <= 215:
            mean = 70
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
        elif 216 <= weight <= 235:
            mean = 80
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
    # height: 6'7 - 7'0
    elif 79 <= height <= 84:
        if 215 <= weight <= 235:
            mean = 60
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
        elif 236 <= weight <= 255:
            mean = 75
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
        elif 256 <= weight <= 275:
            mean = 85
            sd = 8
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
    # height: 7'1 - 7'6
    elif 85 <= height <= 90:
        if 250 <= weight <= 275:
            mean = 70
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
        elif 276 <= weight <= 295:
            mean = 80
            sd = 10
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
        elif 296 <= weight <= 330:
            mean = 90
            sd = 5
            
            skill = np.random.normal(mean, sd)
            skill = np.round(skill).astype(int)
            
            
    if skill < minSkill:
        skill = random.randint(0,15)
    if skill > maxSkill:
        skill = random.randint(95, 100)
        
    return skill
        

    
def VerticalGeneration(height, weight):
    minSkill = 0
    maxSkill = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 6'0
            (68,72): {"mean": 80, "sd": 5},
            # height: 6'1 - 6'6
            (73,78): {"mean": 85, "sd": 6},
            # height: 6'7 - 7'0
            (79,84): {"mean": 75, "sd": 8},
            # height: 7'1 - 7'6
            (85,90): {"mean": 65, "sd": 10},
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
    
    
    
# main function for creating all the attributes of a single player
def PlayerGeneration():
    # name
    name = PlayerNameGeneration()
    
    # height and weight
    heightWeightAndWingspan = PlayerWeightAndHeightGeneration()
    height = heightWeightAndWingspan[0]
    weight = heightWeightAndWingspan[1]
    wingspan = heightWeightAndWingspan[2]
    
    #convert height into inches for skill generation
    feet, inches = height.split("'")
    
    feet = int(feet)
    inches = int(inches)
    
    totalInches = feet * 12 + inches 
    
    # convert wingspan into wingspan difference
    wingspanDifference = wingspan - totalInches
    
    # other physicals
    strength = StrengthGeneration(totalInches, weight)
    vertical = VerticalGeneration(totalInches, weight)
    footwork = FootworkGeneration(totalInches, weight)
    speed = SpeedGeneration(totalInches, weight)
    stamina = StaminaGeneration(totalInches, weight)
    
    # Skills
    offenseSkills = OffenseGeneration.OffenseGeneration(totalInches, weight, wingspanDifference, strength, vertical, footwork, speed, stamina)
    offense = int(offenseSkills[0])
    
    # Add basic characteristics and skill averages to PlayersDetails data frame
    PlayersDetails.loc[len(PlayersDetails)] = [name, height, weight, wingspan, offense]
    
    
    
    # extract advanced skills
    threePointSkill = int(offenseSkills[1])
    midrangeSkill = int(offenseSkills[2])
    freethrowSkill = int(offenseSkills[3])
    postScoringSkill = int(offenseSkills[4])
    layupSkill = int(offenseSkills[5])
    floaterSkill = int(offenseSkills[6])
    dunkSkill = int(offenseSkills[7])
    # add advanced skills to PlayersAdvancedDetails data frame
    physicals = 0
    PlayersAdvancedDetails.loc[len(PlayersAdvancedDetails)] = [name, physicals, height, weight, wingspan, strength, vertical, footwork, speed, stamina, offense, threePointSkill, 
                                                               midrangeSkill, freethrowSkill, postScoringSkill, layupSkill, floaterSkill, dunkSkill]
    
    return name




# LEAGUE
# function called on to generate a new league
def LeagueGeneration(teamAmt, rosterAmt):
    # establish a list of all team rosters assigned by team
    global totalTeamRosters
    totalTeamRosters = []
    
    global PlayersDetails
    PlayersDetails = pd.DataFrame(columns=["Player", "Height", "Weight", "Wingspan", "Offense"])
    global PlayersAdvancedDetails
    PlayersAdvancedDetails = pd.DataFrame(columns=["Player", "Physicals", "Height", "Weight", "Wingspan", "Strength", "Vertical", "Footwork", "Speed", "Stamina", "Offense", 
                                                   "Three Point", "Midrange", "Free Throw", "Post Scoring", "Layups", "Floater", "Dunk"])
    # for loop that creates each team and its roster
    for num in range(teamAmt):
        TeamGeneration()
        
        teamRoster = []
        for num in range(rosterAmt):
            player = PlayerGeneration()
            teamRoster.append(player)
        
        totalTeamRosters.append({"Team": team, "Players": teamRoster})
        
    # create a dataframe for all team roster to better contain this data and for better looking display of the rosters
    global TeamRosterDataFrame
    TeamRosterDataFrame = pd.DataFrame(totalTeamRosters)    
    print(TeamRosterDataFrame)