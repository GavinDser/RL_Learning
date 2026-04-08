import numpy as np
import random

class GridWorld_v1(object):
     
    #gridworld version 1 for deterministic policy iteration and value iteration
    #randommize forbidden area and target area if wanted
    
    #records the state index map
    stateMap = None
    #records the reward map
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
                    # "x" is for forbidden area, "!" is for target area, other position is "."
                    temp.append(forbiddenAreaVal if fixed[i][j] == "x" else targetAreaVal if fixed[i][j] == "!" else 0)
                m.append(temp)
            
            self.scoreMap = np.array(m)
            self.stateMap = [[i*self.columns+j for j in range(self.columns)] for i in range(self.rows)]
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
        self.stateMap = [[i*self.columns+j for j in range(self.columns)] for i in range(self.rows)]
        
        
            
    
    
    def show_map(self):
        print("[Grid World Map]")
        for i in range(self.rows):
            l = ""
            for j in range(self.columns):
                tmp = {0:"🟪",self.targetAreaVal:"✅",self.forbiddenAreaVal:"❌"}
                l = l+tmp[self.scoreMap[i][j]]
            print(l)
                
                
    #Includes 5 action, from 0 to 4
    #a0:up
    #a1:right
    #a2:down
    #a3:left
    #a4:stay
    def step(self, currentState, action):
        currentX = currentState // self.columns
        currentY = currentState % self.columns
        
        if (currentX < 0 or currentY < 0 or currentX >= self.rows or currentY >= self.columns):
            print(f"Coordinate Error: ({currentX},{currentY})")
        if (action<0 or action > 4):
            print(f"Wrong action: {action}")
        
        
        actionList = [(-1,0),(0,1),(1,0),(0,-1),(0,0)]
        tempX = currentX + actionList[action][0]
        tempY = currentY + actionList[action][1]
        
        #check for outbounds
        if (tempX < 0 or tempX >= self.rows or tempY < 0 or tempY >= self.columns):
            return -1, currentState
        
        #return immediate reward and next state
        return self.scoreMap[tempX][tempY], self.stateMap[tempX][tempY]
    
    
    
    
    def show_policy(self, policy):
        print("[Policy Map]")
        rows = self.rows
        columns = self.columns
        s = ""
        
        for i in range(self.rows * self.columns):
            currentX = i // columns
            currentY = i % columns
            
            if(self.scoreMap[currentX][currentY] == self.targetAreaVal):
                s = s + "✅"
            if(self.scoreMap[currentX][currentY]==0):
                temp = {0:"⬆️",1:"➡️",2:"⬇️",3:"⬅️",4:"🔄"}
                s = s + temp[policy[i]]
            if(self.scoreMap[currentX][currentY]==self.forbiddenAreaVal):
                temp = {0:"⏫️",1:"⏩️",2:"⏬",3:"⏪",4:"🔄"}
                s = s + temp[policy[i]]
            if(currentY == columns-1):
                print(s)
                s = ""