from player import *
from npc import *
import random
import sys

class Professor (NPC):
    
    def __init__ (self,name,loc,restlessness,professorial,desc):
        NPC.__init__(self,name,loc,restlessness,100, desc)
        self._professorial = professorial
        Player.clock.register(self.lecture,2,Player.clock.time)       
        self._topics = ['Turing machines',
                 'the lambda calculus',
                 'Godel']
    
    def lecture (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._professorial) == 0:
                if self.people_around():
                    self.location().report(self.name()+' starts lecturing about '+random.choice(self._topics))
                else:
                    self.location().report(self.name()+' mutters to himself about '+random.choice(self._topics))
    
    def grade_homework(self,hw,actor):
        self.say( "Hmmm.... Let's check this homework.")
        if hw.check_done_homework():
            self.say("mmm.... Very nice....")
            self.say("You win!!!")
            sys.exit(0)
        else:
            self.say("Wait... This homework is not even started!!")
            hw.give(self,actor)
              
    def is_professor(self):
        return True
          
    def die(self):
        Player.clock.register(self.lecture,2,Player.clock.time)       
        NPC.die(self)