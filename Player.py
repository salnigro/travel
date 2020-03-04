import random
class Player(object):
    self.path1 = [1,3,5,7,9,11,13,15,17,19]
    self.path2 = [2,4,6,8,10,12,14,16,18,20]
    self.path3 = [21,31,41,51]
    self.path4 = [1,2]
    self.saved = []
    def __init__(self,name,health,gold,):
        self.name = name
        self.health = health
        s = random(0,2)
        if(s==0):
            self.sword = sword(1,1)
            self.shield = shield(0,0)
        else:
            self.shield = shield(1,1)
            self.sword = sword(0,0)

    def choosePath(self):
        t = input("choose search house or leave " + str(self.path1) + "/" + str(self.path2))
        if(int(t) == 1):
            self.path1.pop(0)
            self.path2.pop(0)
            self.pathone(t)
        
        

    def pathone(self,t):
        s = random(1,101)
        if(s > 98):
            t = self.path3(0)
            self.path3.pop(0)
        if(t == 1):
            print("you walk down left path")
            print("you see a unconsious person and a box")
            print("rob and leave or help(1/2)")
            
