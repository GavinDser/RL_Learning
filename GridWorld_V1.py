import numpy as np
import random

class GridWorld_v1(object):
     
    #gridworld version 1 for deterministic policy iteration and value iteration
    #randommize forbidden area and target area if wanted
    
    scoreMap = None
    
    targetAreaVal = 0
    forbiddenAreaVal = 0
    
    def __init__(self, rows = 5,columns = 5, forbiddenAreaNums = 3, targetNums = 1, targetAreaVal = 1, forbiddenAreaVal = -1, seed = -1, fixed = None):
        self.targetAreaVal = targetAreaVal
        self.forbiddenAreaVal = forbiddenAreaVal
        self.seed = seed
        self.forbiddenAreaNums = forbiddenAreaNums
        self.targetNums = targetNums
        
        if (fixed != None):
            self.rows = len(fixed)
            self.columns = len(fixed[0])
            m = []
            for i in range(self.rows):
                temp = []
                for j in range(self.columns):
                    # "x" is for forbidden area, "!" is for target area, other position is "0"
                    temp.append(forbiddenAreaVal if fixed[i][j] == "x" else targetAreaVal if fixed[i][j] == "!" else 0)
                m.append(temp)
            
            self.scoreMap = np.array(m)
            return
            
            
            
        
        
        #random world
        self.rows = rows
        self.columns = columns
        # use to random all the positions
        self.randomNums = forbiddenAreaNums + targetNums


        random.seed(self.seed)
        m = [0 for i in range(self.rows*self.columns)]
        
        randomPos = random.sample(range(self.rows * self.columns), self.randomNums)
        
        
        for i in range(len(randomPos)):
            if i >= self.forbiddenAreaNums:
                m[randomPos[i]] = self.targetAreaVal
            
            else:
                m[randomPos[i]] = self.forbiddenAreaVal
            
        self.scoreMap = np.array(m).reshape(self.rows,self.columns)
        
        
            
    
    
    def show_map(self):
        print("[Grid World Map]")
        for i in range(self.rows):
            l = ""
            for j in range(self.columns):
                tmp = {0:"🟪",self.targetAreaVal:"✅",self.forbiddenAreaVal:"❌"}
                l = l+tmp[self.scoreMap[i][j]]
            print(l)
                