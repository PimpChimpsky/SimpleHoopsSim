# import random
# import numpy as np

# def HeightAndWeightGeneration():
#     minHeight = 68
#     maxHeight = 90
    
#     minWeight = 170
#     maxWeight = 325
    
#     minWingspan = 65
#     maxWingspan = 97
    
    
#     # height generation
#     meanHeight = 79
#     stdDevHeight = 4
    
#     height = np.random.normal(meanHeight, stdDevHeight)
#     height = np.round(height).astype(int)
    
#     if height>maxHeight:
#         height = random.randint(87, 90)
#     elif height<minHeight:
#         height = random.randint(68, 71)
        
#     # weight generation
    
#     # BLAH BLAH BLAH
    
    
    
# # skillParameters = [
# #     {"heightRange": (68,69), "weightRange": (170,190), "wingspanRange": (65,76)},
# #     {}
# # ] 
# skillParameters = {
#         "heightRange": {
#             (68,69): {"mean": 76, "sd": 5}
#             # more heights
#         },
#         "weightRange": {
#             (170,180): {"mean": 76, "sd": 5}
#             # more weights
#         },
#         "wingspanRange": {
#             (65, 76): {"mean": 65, "sd": 10}
#             # more wingspans
#         }
#     }   
 
# def midrangeSkillGeneration(height, weight, wingspan):
#     minSkill = 0
#     maxSkill = 100
    
#     heightParameters = GetParameters(height, "heightRange")
#     weightParamaters = GetParameters(weight, "weightRange")
#     wingspanParameters = GetParameters(wingspan, "wingspanRange")
    
#     combinedMean = heightParameters["mean"] + weightParamaters["mean"] + wingspanParameters["mean"] / 3
#     combinedSD = heightParameters["sd"] + weightParamaters["sd"] + wingspanParameters["sd"] / 3
    
#     skill = np.random.normal(combinedMean, combinedSD)
#     skill = np.round(skill).astype(int)
    
#     if skill > maxSkill:
#         skill = random.randint(95, 100)
#     if skill < minSkill:
#         skill = random.randint(0, 10)
    
    
# def GetParameters(value, parameter_type):
#     # Look up the parameters based on the specified value and parameter type
#     for value_range, params in skillParameters[parameter_type].items():
#         if value_range[0] <= value <= value_range[1]:
#             return params
    
    
#     # i=0
#     # for sizeRange in sizeRanges:
#     #     heightRange = sizeRange["heightRange"]
#     #     weightRange = sizeRange["weightRange"]
#     #     wingspanRange = sizeRange["wingspanRange"]
        
#     # if heightRange[0] <= height <= heightRange[1] and \
#     #     weightRange[0] <= weight <= weightRange[1] and \
#     #     wingspanRange[0] <= wingspan <= wingspanRange[1]:
            
#     #         if i = 0:
                
                
                
class testing:
    def addition():
        a = testing.userInput()
        b = testing.userInput()
        
        return a+b
    
    def userInput():
        a = random.rad