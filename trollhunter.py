import random
from npc import *

class TrollHunter(NPC):
    def __init__ (self,name,loc,restlessness,rage,desc):
        NPC.__init__(self,name,loc,restlessness,10, desc)
        self._rage = rage
        
    def rage(self):
        return self._rage
        
    def set_rage(self,rage):
        self._rage = rage
        
    def kill_trolls (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._rage) == 0:
            troll = self.trolls_around()
            if troll:
                prey = random.choice(troll)
                self.location().report(self.name() + ' hunts down ' + prey.name())
                prey.suffer(random.randint(1,5))
            else:
                self.location().report(self.name() + " is full of rage!!!")

