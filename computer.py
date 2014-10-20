from thing import *


class Computer (Thing):
    def __init__ (self,name,loc, desc):
        Thing.__init__(self,name,loc, desc)

    def use (self,actor):
        for content in actor.contents():
            if content.is_homework():
                actor.say('I use '+self.name()+' and it completes my '+ content.name())
                content.is_done_homework()
                old_name = content.name()
                content.set_Name("done-"+old_name)
        
                
    
        
                