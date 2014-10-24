# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 14:50:18 2014

@author: jmorris
"""

from npc import *
from player import *

class BadNinja(NPC):
    def __init__(self,name,loc,restlessness,miserly,desc):
        NPC.__init__(self,name,loc,restlessness,3, desc)
        self._max_health = 10
        self._health = self._max_health
        self.miserly = miserly
        Player.clock.register(self.steal,2,Player.clock.time)
    
    def is_player():
        return False
        
    def steal(self,time):
        if not self.is_in_limbo() and self.location()==Player.me.location():
            for content in Player.me.contents():
                if content.is_homework():
                    content.take2(self,Player.me)
                    self.say("Time to BURN your homework!!")
                    content.destroy()
                    print "Your homework was burned by the bad ninja."
            
            stuff =[]
            stuff.extend(self.stuff_around())
            for content in stuff:
                if content.is_homework() and random.randrange(self._miserly) == 0:
                    content.take1(self)
                    self.say("Burn all homework!!.")
                    content.destroy()
                    print content.name()+" was destroyed."
                    
    def is_badninja():
        return True
