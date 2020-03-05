from Npc import Npc
from Town import Town
from Player import Player
from Road import Road
import math  
class World(object):
    
    def __init__(self,player):
        self.player = player
        self.npcs = [Npc(1),Npc(2),Npc(3),Npc(4)]
        self.towns = [Town(self.npcs,"0",[0,0]),Town(self.npcs,"1",[1,1]),Town(self.npcs,"2",[2,2]),
                      Town(self.npcs,"3",[3,3]),Town(self.npcs,"4",[4,4]),Town(self.npcs,"5",[5,5]),
                      Town(self.npcs,"6",[6,6]),Town(self.npcs,"7",[7,7]),Town(self.npcs,"8",[8,8])]
    def menu(self):
        start = self.player.location
        for i in range(len(self.towns)):
            st = self.towns[i].location
            if(math.sqrt((st[0]-start[0])*(st[0]-start[0]) + (st[1]-start[1])*(st[1]-start[1])) < 2):
                print(str(i) + ": " + self.towns[i].name)
        t = input("where to ")

        self.player.location = self.towns[int(t)].roads[0].start
        
        self.towns[int(t)].menu(self.player.location)
        self.player.location = self.towns[int(t)].location
        self.menu()
