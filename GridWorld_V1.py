import numpy as np
import random

class GridWorld_v1(object):
     
    #gridworld version 1 for deterministic policy iteration and value iteration
    #randommize forbidden area and target area if wanted
    
    stateMap = None
    scoreMap = None

    def __init__(self, rows = 4):
        pass