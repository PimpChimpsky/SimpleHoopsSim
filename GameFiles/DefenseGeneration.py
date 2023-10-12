import time
import multiprocessing
import random
import numpy as np
import pandas as pd

class defenseGeneration:
    def __init__(self, height, weight, wingspan, strength, vertical, footwork, speed, stamina):
        self.height = height
        self.weight = weight
        self.wingspan = wingspan
        self.strength = strength
        self.vertical = vertical
        self.footwork = footwork
        self.speed = speed
        self.stamina = stamina
        
        minLevel = 0
        maxLevel = 100
        
        def perimeterDefenseGeneration(weight, wingspan, strength, speed):
            skillParameters = {
            "weightRange": {
                
            },
            "wingspanRange": {
                (-4, -1): {"mean": 85, "sd": 5},
                (0, 3): {"mean": 75, "sd": 6},
                (4, 5): {"mean": 65, "sd": 8},
                (6, 8): {"mean": 50, "sd": 10},
            },
            "strengthRange": {
                
            },
            "speedRange": {
                
            }
        } 