from thing import *

class MobileThing (Thing):

    def __init__ (self,name,loc,desc):
        Thing.__init__(self,name,loc,desc)
        self._original_location = loc


    def creation_site (self):
        return self._original_location
    
    def move (self,loc):
        self.location().del_thing(self)
        loc.add_thing(self)
        self._location = loc
        
    def take1(self,actor):
        if actor.have_thing(self)==True:
            actor.say('I already have' + self.name())
        else:
            actor.say('I took ' + self.name())
            actor.location().del_thing(self)
            actor.add_thing(self)
    
    def drop(self,actor):
        actor.say('I drop ' + self.name() +' at '+ actor.location().name() )
        actor.del_thing(self)
        actor.location().add_thing(self)

    
    def give(self, actor, acted):
        if self in actor.contents():
            actor.say('I gave ' + self.name() + ' to ' + acted.name())
            actor.del_thing(self)
            acted.add_thing(self)
            
        else:
            actor.say('I do not have ' + self.name())
    
    def take2(self, actor, acted):
        if self in acted.contents():
            actor.say('I took ' + self.name() + ' from ' + acted.name())
            actor.add_thing(self)
            acted.del_thing(self)
            acted.say(' Yaarg!! I am upset!!')
        
        else:
            actor.say(acted.name() + ' does not have ' + self.name())

    def is_mobile_thing (self):
        return True







