import random
import numpy as np
import pandas as pd

def GetParameters(value, parameter_type, parameter):
    # Look up the parameters based on the specified value and parameter type
    for value_range, params in parameter[parameter_type].items():
        if value_range[0] <= value <= value_range[1]:
            return params


# generate offensive skill level
def OffenseGeneration(height, weight, wingspan, strength, vertical, footwork, speed, stamina):
    #set minimum and maximum skill level
    minLevel = 0
    maxLevel = 100   
    
    # run different skill functions
    ThreePointSkill = ThreePointGeneration(height, wingspan)
    MidrangeSkill = MidRangeGeneration(height,wingspan)
    FreeThrowSkill = FreeThrowGeneration(height, wingspan)
    PostScoringSkill = PostScoringGeneration(height, wingspan, weight)
    LayupSkill = LayupsGeneration(wingspan, speed, footwork)
    FloaterSkill = FloaterGeneration(wingspan, speed, footwork)
    DunkSkill = DunkGeneration(wingspan, strength, vertical, footwork)
    
    offenseAvg = (ThreePointSkill + MidrangeSkill + FreeThrowSkill + PostScoringSkill + LayupSkill + FloaterSkill + DunkSkill) / (7)
    offenseAvg = np.round(offenseAvg).astype(int)
    offense = [offenseAvg, ThreePointSkill, MidrangeSkill, FreeThrowSkill, PostScoringSkill, LayupSkill, FloaterSkill, DunkSkill]
    
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



def LayupsGeneration(wingspan, speed, footwork):
    minSkill = 0
    maxSkill = 100
    
    skillParameters = {
        "speedRange": {
            (0,20): {"mean": 50, "sd": 10},
            (21,40): {"mean": 60, "sd": 10},
            (41,60): {"mean": 70, "sd": 5},
            (61,70): {"mean": 75, "sd": 5},
            (71,80): {"mean": 80, "sd": 5},
            (81,90): {"mean": 85, "sd": 5},
            (91,95): {"mean": 90, "sd": 5},
            (96,100): {"mean": 95, "sd": 5},
        },
        "wingspanRange": {
            (-4, -1): {"mean": 75, "sd": 5},
            (0, 3): {"mean": 80, "sd": 5},
            (4, 5): {"mean": 85, "sd": 5},
            (6, 8): {"mean": 90, "sd": 5},
        },
        "footworkRange": {
            (0,20): {"mean": 50, "sd": 10},
            (21,40): {"mean": 60, "sd": 10},
            (41,60): {"mean": 70, "sd": 5},
            (61,70): {"mean": 75, "sd": 5},
            (71,80): {"mean": 80, "sd": 5},
            (81,90): {"mean": 85, "sd": 5},
            (91,95): {"mean": 90, "sd": 5},
            (96,100): {"mean": 95, "sd": 5},
        }
    }
    
    speedParameters = GetParameters(speed, "speedRange", skillParameters)
    wingspanParameters = GetParameters(wingspan, "wingspanRange", skillParameters)
    footworkParameters = GetParameters(footwork, "footworkRange", skillParameters)
    
    
    combinedMean = speedParameters["mean"] + wingspanParameters["mean"] + footworkParameters["mean"]
    combinedMean = combinedMean / 3
    combinedSD = speedParameters["sd"] + wingspanParameters["sd"] + footworkParameters["sd"]
    combinedSD = combinedSD / 3
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxSkill:
        skill = random.randint(95, 100)
    if skill < minSkill:
        skill = random.randint(0, 10)
        
    return skill


def FloaterGeneration(wingspan, speed, footwork):
    minSkill = 0
    maxSkill = 100

    skillParameters = {
        "speedRange": {
            (0,20): {"mean": 60, "sd": 10},
            (21,40): {"mean": 65, "sd": 10},
            (41,60): {"mean": 70, "sd": 5},
            (61,70): {"mean": 75, "sd": 5},
            (71,80): {"mean": 80, "sd": 5},
            (81,90): {"mean": 85, "sd": 5},
            (91,95): {"mean": 90, "sd": 5},
            (96,100): {"mean": 95, "sd": 5},
        },
        "wingspanRange": {
            (-4, -1): {"mean": 75, "sd": 5},
            (0, 3): {"mean": 80, "sd": 5},
            (4, 5): {"mean": 85, "sd": 5},
            (6, 8): {"mean": 90, "sd": 5},
        },
        "footworkRange": {
            (0,20): {"mean": 50, "sd": 10},
            (21,40): {"mean": 60, "sd": 10},
            (41,60): {"mean": 70, "sd": 5},
            (61,70): {"mean": 75, "sd": 5},
            (71,80): {"mean": 80, "sd": 5},
            (81,90): {"mean": 85, "sd": 5},
            (91,95): {"mean": 90, "sd": 5},
            (96,100): {"mean": 95, "sd": 5},
        }
    }
    
    speedParameters = GetParameters(speed, "speedRange", skillParameters)
    wingspanParameters = GetParameters(wingspan, "wingspanRange", skillParameters)
    footworkParameters = GetParameters(footwork, "footworkRange", skillParameters)
    
    
    combinedMean = speedParameters["mean"] + wingspanParameters["mean"] + footworkParameters["mean"]
    combinedMean = combinedMean / 3
    combinedSD = speedParameters["sd"] + wingspanParameters["sd"] + footworkParameters["sd"]
    combinedSD = combinedSD / 3
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxSkill:
        skill = random.randint(95, 100)
    if skill < minSkill:
        skill = random.randint(0, 10)
        
    return skill



def DunkGeneration(wingspan, strength, vertical, footwork):
    minSkill = 0
    maxSkill = 100
    
    skillParameters = {
        "wingspanRange": {
            (-4, -1): {"mean": 65, "sd": 5},
            (0, 3): {"mean": 80, "sd": 5},
            (4, 5): {"mean": 85, "sd": 5},
            (6, 8): {"mean": 90, "sd": 5},
        },
        "strengthRange": {
            (0,20): {"mean": 50, "sd": 10},
            (21,40): {"mean": 60, "sd": 10},
            (41,60): {"mean": 70, "sd": 5},
            (61,70): {"mean": 75, "sd": 5},
            (71,80): {"mean": 80, "sd": 5},
            (81,90): {"mean": 85, "sd": 5},
            (91,95): {"mean": 90, "sd": 5},
            (96,100): {"mean": 95, "sd": 5},
        },
        "verticalRange": {
            (0,20): {"mean": 25, "sd": 10},
            (21,40): {"mean": 45, "sd": 10},
            (41,60): {"mean": 65, "sd": 5},
            (61,70): {"mean": 75, "sd": 5},
            (71,80): {"mean": 80, "sd": 5},
            (81,90): {"mean": 88, "sd": 5},
            (91,95): {"mean": 90, "sd": 5},
            (96,100): {"mean": 95, "sd": 5},
        },
        "footworkRange": {
            (0,20): {"mean": 50, "sd": 10},
            (21,40): {"mean": 60, "sd": 10},
            (41,60): {"mean": 70, "sd": 5},
            (61,70): {"mean": 75, "sd": 5},
            (71,80): {"mean": 80, "sd": 5},
            (81,90): {"mean": 85, "sd": 5},
            (91,95): {"mean": 90, "sd": 5},
            (96,100): {"mean": 95, "sd": 5},
        }
    }
    
    wingspanParameters = GetParameters(wingspan, "wingspanRange", skillParameters)
    strengthParameters = GetParameters(strength, "strengthRange", skillParameters)
    verticalParameters = GetParameters(vertical, "verticalRange", skillParameters)
    footworkParameters = GetParameters(footwork, "footworkRange", skillParameters)
    
    
    combinedMean = wingspanParameters["mean"] + strengthParameters["mean"] + verticalParameters["mean"] + footworkParameters["mean"]
    combinedMean = combinedMean / 4
    combinedSD = wingspanParameters["sd"] + strengthParameters["sd"] + verticalParameters["sd"] + footworkParameters["sd"]
    combinedSD = combinedSD / 4
    
    skill = np.random.normal(combinedMean, combinedSD)
    skill = np.round(skill).astype(int)
    
    if skill > maxSkill:
        skill = random.randint(95, 100)
    if skill < minSkill:
        skill = random.randint(0, 10)
        
    return skill