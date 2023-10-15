# This file is called upon to generate a whole league
import pandas as pd
from GameFiles.Offense import OffensiveGeneration
from GameFiles.playerGenerator import PlayerNameGeneration, PlayerWeightAndHeightGeneration, StrengthGeneration, VerticalGeneration, FootworkGeneration, SpeedGeneration, StaminaGeneration
from GameFiles.teamGenerator import TeamGeneration
import pandas as pd
from pathlib import Path


parent_dir = Path(__file__).parent.parent


# Define global variables for Player details
PlayersDetails = pd.DataFrame(columns=["Player", "Height", "Weight", "Wingspan", "Offense"])
PlayersAdvancedDetails = pd.DataFrame(columns=["Player", "Physicals", "Height", "Weight", "Wingspan", "Strength", "Vertical", "Footwork", "Speed", "Stamina", "Offense",
                                               "Three Point", "Midrange", "Free Throw", "Post Scoring", "Layups", "Floater", "Dunk"])
    

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
    # offenseSkills = offense.OffenseGeneration(totalInches, weight, wingspanDifference, strength, vertical, footwork, speed, stamina)
    offenseSkills = OffensiveGeneration.OffenseGeneration(totalInches, weight, wingspanDifference, strength, vertical, footwork, speed, stamina)
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
        team = TeamGeneration()
        teamRoster = []

        for num in range(rosterAmt):
            player = PlayerGeneration()
            teamRoster.append(player)
        
        totalTeamRosters.append({"Team": team, "Players": teamRoster})
        
    # create a dataframe for all team roster to better contain this data and for better looking display of the rosters, then save it to /output/teamname.csv with the team name and teams roster
    global TeamRosterDataFrame
    TeamRosterDataFrame = pd.DataFrame(totalTeamRosters)
    TeamRosterDataFrame.to_csv(parent_dir / 'output' / 'teamrosters.csv', index=False)
    
    print(TeamRosterDataFrame)
