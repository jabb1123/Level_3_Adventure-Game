from mobile import *
from npc import *
from player import *


class Caterpillar(MobileThing):
    def __init__(self,age,name,loc,desc):
        MobileThing.__init__(self,name,loc, desc)
        self._age = age
        self._name = name
        self._isCaterpillar = True
        self._isCocoon = False
        
    def age(self):
        return self._age
    
    def is_cocoon(self):
        return self._isCocoon
        
    def is_caterpillar(self):
        return self._isCaterpillar
    
    def new_age(self,time):
        self._age = time
    
    def transform (self):
        if self.age() >= 3:
            if self._isCocoon == True:
                if self.location().is_person():
                    Butterfly(self.name(), self.location().location(),random.randint(1,5),self.name+' is fluttering around!')
                    Player.clock.unregister(self.new_age,1,0)
                    Player.clock.unregister(self.transform,1,None)
                else:
                    Butterfly(self.name(), self.location(),random.randint(1,5),self.name+' is fluttering around!')
                    Player.clock.unregister(self.new_age,1,0)
                    Player.clock.unregister(self.transform,1,None)
                self.destroy()
            else:
                self.is_cocoon = True
                self.setDesc(self.name()+' has become a cocoon!')
                
                
                
        
class Butterfly(NPC):
    def __init__ (self,name,loc,restlessness, desc):
        NPC.__init__(self,name,loc, desc,restlessness,0,desc)
        Player.clock.register(self.move_and_take_stuff,1,0)
        
    