from npc import *
from player import *

class Babo(NPC):
    def __init__(self,name,loc,restlessness,justice,desc):
        NPC.__init__(self,name,loc,restlessness,1,desc)
        self._justice = justice
        
        def is_babo(self):
            return True
        
        def detain(self,time):
            if not self.is_in_limbo():
                if random.randrange(self._hunger) == 0:
                    people = self.people_around()
                    if people:
                        criminal = random.choice(people)
                        self.location().report(self.name() + ' arrests ' + criminal.name())
                        criminal.suffer(random.randint(1,3))
                    else:
                        self.location().report(self.name() + "'s belly rumbles")
