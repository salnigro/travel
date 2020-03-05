from Npc import Npc
from Road import Road
class Town(object):
    def __init__(self,npc,name,location):
        #self.shop = shop
        self.npc = npc
        self.name = name
        self.location = location
        self.roads = [Road("0 rd",[0,0],[0,4]),Road("1 rd",[0,1],[-1,1]),
                      Road("2 rd",[-1,1],[-1,2]),Road("3 rd",[0,3],[-1,2]),
                      Road("4 rd",[-1,2],[0,3]),Road("5 rd",[0,2],[1,2]),
                      Road("6 rd",[0,4],[1,4]),Road("7 rd",[1,4],[1,3])]
    
    
        
    def menu(self,st):
        #print(self.name)
        #updw = []
        #ltrt = []
        for i in range(0,len(self.roads)):
            if(st[0] == self.roads[i].start[0]):
                #updw.append(i)
                print(str(i) + " " + self.roads[i].name)
            if(st[1] == self.roads[i].start[1]):
                #ltrt.append(i)
                print(str(i) + " " + self.roads[i].name)
        
        #for i in range(len(updw)):
           # print(str(i)  + " " + self.roads[updw[i]].name)
        t = input("where to")
        st = self.roads[int(t)].start
        if(int(t) != 10):
            self.menu()
  
        
        
