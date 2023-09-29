import random
import numpy as np
import pandas as pd

def GetParameters(value, parameter_type, parameter):
    # Look up the parameters based on the specified value and parameter type
    for value_range, params in parameter[parameter_type].items():
        if value_range[0] <= value <= value_range[1]:
            return params


# generate offensive skill level
def OffenseGeneration(height, weight, wingspanDifference):
    #set minimum and maximum skill level
    minLevel = 0
    maxLevel = 100   
    
    # run different skill functions
    ThreePointSkill = ThreePointGeneration(height, wingspanDifference)
    MidrangeSkill = MidRangeGeneration(height,wingspanDifference)
    FreeThrowSkill = FreeThrowGeneration(height, wingspanDifference)
    PostScoringSkill = PostScoringGeneration(height, wingspanDifference, weight)
    
    offenseAvg = (ThreePointSkill + MidrangeSkill + FreeThrowSkill + PostScoringSkill) / (4)
    offenseAvg = np.round(offenseAvg).astype(int)
    
    offense = [offenseAvg, ThreePointSkill, MidrangeSkill, FreeThrowSkill, PostScoringSkill]
    
    return offense

 
 
def ThreePointGeneration(height, wingspan):
    minLevel = 0
    maxLevel = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 6'0
            (68,72): {"mean": 80, "sd": 5},
            # height: 6'1 - 6'6
            (73,78): {"mean": 75, "sd": 6},
            # height: 6'7 - 7'0
            (79,84): {"mean": 65, "sd": 8},
            # height: 7'1 - 7'6
            (85,90): {"mean": 50, "sd": 10},
        },
        "wingspanRange": {
            (-4, -1): {"mean": 85, "sd": 5},
            (0, 3): {"mean": 75, "sd": 6},
            (4, 5): {"mean": 65, "sd": 8},
            (6, 8): {"mean": 50, "sd": 10},
        }
    } 
    
    heightParameters = GetParameters(height, "heightRange", skillParameters)
    wingspanParameters = GetParameters(wingspan, "wingspanRange", skillParameters)
    
    combinedMean = heightParameters["mean"] + wingspanParameters["mean"]
    combinedMean = combinedMean / 2
    combinedSD = heightParameters["sd"] + wingspanParameters["sd"]
    combinedSD = combinedSD / 2
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxLevel:
        skill = random.randint(95, 100)
    if skill < minLevel:
        skill = random.randint(0, 10)
        
    return skill 

 
 
def MidRangeGeneration(height, wingspan):
    minLevel = 0
    maxLevel = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 6'0
            (68,72): {"mean": 75, "sd": 6},
            # height: 6'1 - 6'6
            (73,78): {"mean": 80, "sd": 5},
            # height: 6'7 - 7'0
            (79,84): {"mean": 70, "sd": 6},
            # height: 7'1 - 7'6
            (85,90): {"mean": 60, "sd": 8},
        },
        "wingspanRange": {
            (-4, -1): {"mean": 80, "sd": 6},
            (0, 3): {"mean": 80, "sd": 5},
            (4, 5): {"mean": 70, "sd": 6},
            (6, 8): {"mean": 60, "sd": 8},
        }
    } 
    
    heightParameters = GetParameters(height, "heightRange", skillParameters)
    wingspanParameters = GetParameters(wingspan, "wingspanRange", skillParameters)
    
    combinedMean = heightParameters["mean"] + wingspanParameters["mean"]
    combinedMean = combinedMean / 2
    combinedSD = heightParameters["sd"] + wingspanParameters["sd"]
    combinedSD = combinedSD / 2
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxLevel:
        skill = random.randint(95, 100)
    if skill < minLevel:
        skill = random.randint(0, 10)
        
    return skill



def FreeThrowGeneration(height, wingspan):
    minLevel = 0
    maxLevel = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 6'0
            (68,72): {"mean": 85, "sd": 5},
            # height: 6'1 - 6'6
            (73,78): {"mean": 80, "sd": 6},
            # height: 6'7 - 7'0
            (79,84): {"mean": 75, "sd": 8},
            # height: 7'1 - 7'6
            (85,90): {"mean": 65, "sd": 10},
        },
        "wingspanRange": {
            (-4, -1): {"mean": 85, "sd": 5},
            (0, 3): {"mean": 80, "sd": 6},
            (4, 5): {"mean": 65, "sd": 8},
            (6, 8): {"mean": 55, "sd": 10},
        }
    } 
    
    heightParameters = GetParameters(height, "heightRange", skillParameters)
    wingspanParameters = GetParameters(wingspan, "wingspanRange", skillParameters)
    
    combinedMean = heightParameters["mean"] + wingspanParameters["mean"]
    combinedMean = combinedMean / 2
    combinedSD = heightParameters["sd"] + wingspanParameters["sd"]
    combinedSD = combinedSD / 2
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxLevel:
        skill = random.randint(95, 100)
    if skill < minLevel:
        skill = random.randint(0, 10)
        
    return skill



def PostScoringGeneration(height, wingspan, weight):
    minLevel = 0
    maxLevel = 100
    
    skillParameters = {
        "heightRange": {
            # height: 5'8 - 5'11
            (68,71): {"mean": 15, "sd": 5},
            # height: 6'0 - 6'1
            (72,73): {"mean": 20, "sd": 5},
            # height: 6'2 - 6'3
            (74,75): {"mean": 40, "sd": 5},
            # height: 6'4 - 6'5
            (76,77): {"mean": 50, "sd": 5},
            # height: 6'6 - 6'7
            (78,79): {"mean": 65, "sd": 5},
            # height: 6'8 - 6'9
            (80,81): {"mean": 75, "sd": 5},
            # height: 6'10 - 6'11
            (82,83): {"mean": 80, "sd": 5},
            # height: 7'0 - 7'1
            (84,85): {"mean": 85, "sd": 5},
            # height: 7'2 - 7'3
            (86,87): {"mean": 85, "sd": 5},
            # height: 7'4 - 7'6
            (88,90): {"mean": 85, "sd": 5},
        },
        "weightRange": {
            (170,190): {"mean": 20, "sd": 5},
            (191,210): {"mean": 35, "sd": 5},
            (211,230): {"mean": 50, "sd": 5},
            (231,250): {"mean": 60, "sd": 5},
            (251,270): {"mean": 70, "sd": 5},
            (271,290): {"mean": 75, "sd": 5},
            (291,310): {"mean": 80, "sd": 5},
            (311,330): {"mean": 85, "sd": 5},
        },
        "wingspanRange": {
            (-4, -1): {"mean": 40, "sd": 5},
            (0, 3): {"mean": 55, "sd": 5},
            (4, 5): {"mean": 80, "sd": 5},
            (6, 8): {"mean": 85, "sd": 5},
        }
    } 
    
    heightParameters = GetParameters(height, "heightRange", skillParameters)
    weightParamaters = GetParameters(weight, "weightRange", skillParameters)
    wingspanParameters = GetParameters(wingspan, "wingspanRange", skillParameters)
    
    combinedMean = heightParameters["mean"] + weightParamaters["mean"] + wingspanParameters["mean"]
    combinedMean = combinedMean / 3
    combinedSD = heightParameters["sd"] + weightParamaters["sd"] + wingspanParameters["sd"]
    combinedSD = combinedSD / 3
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxLevel:
        skill = random.randint(95, 100)
    if skill < minLevel:
        skill = random.randint(0, 10)
        
    return skill