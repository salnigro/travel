
class Npc(object):
    def __init__(self,quest):
        self.quest = quest
        self.cpm = 0;

    def speech(self):
        if(cpm == 0):
            t = input("I need your help adventurer (y/n)")
            if(t == "y"):
                print("Thanks you adventure i need you to do " + str(self.quest))
            
        if(self.cpm == 1):
            print("thanks")
           
