# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 14:50:18 2014

@author: jmorris
"""

from npc import *


class BadNinja(NPC):
    def __init__(self,name,loc,restlessness,miserly,desc):
        NPC.__init__(self,name,loc,restlessness,3, desc)
        self.miserly = miserly
    
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
            
            
            
   
            
    """    
     def move_and_take_stuff (self,time):
        if not self.is_in_limbo():
            if random.randrange(self._restlessness) == 0:
                self.move_somewhere()
            if random.randrange(self._miserly) == 0:
                self.take_something()


    def take_something (self):
        everything = []
        everything.extend(self.stuff_around())
        everything.extend(self.peek_around())
        if everything:
            something = random.choice(everything)
            something.take(self)
    
    def use (self,actor):
        for content in actor.contents():
            if content.is_homework():
                actor.say('I use '+self.name()+' and it completes my '+ content.name())
                content.is_done_homework()
                old_name = content.name()
                content.set_Name("done-"+old_name)
    """
                  
            
            
            
            
            
            
            
            
            
            
            
        