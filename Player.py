class Player(object):
    def __init__(self,name,health,gold,location):
        
        self.name = name
        self.health = health
        self.gold = gold
        self.quests = []
        self.exp = 0
        self.location = location
        #s = input("sword or shield. (1/2) ")
        #if(s==1):
            #self.sword = sword(1,1)
            #self.shield = shield(0,0)
        #else:
            #self.shield = shield(1,1)
            #self.sword = sword(0,0)

    
    
