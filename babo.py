from npc import *
from player import *
from room import *

class Babo(NPC):
    def __init__(self,name,loc,restlessness,justice,desc):
        NPC.__init__(self,name,loc,restlessness,1,desc)
        self._justice = justice
        Player.clock.register(self.detain,2,Player.clock.time)
        
    def is_babo(self):
        return True
        
    def detain(self,time):
        if not self.is_in_limbo():
            if random.randrange(self._justice) == 0:
                people = self.people_around()
                if people:
                    criminal = random.choice(people)
                    self.location().report(self.name() + ' arrests ' + criminal.name())
                    criminal.detain(self, Room.rooms[-1])
                else:
                    self.location().report(self.name() + " is looking for bad guys to bust!")

    def die (self):
        Player.clock.unregister(self.detain,2,Player.clock.time)
        NPC.die(self)