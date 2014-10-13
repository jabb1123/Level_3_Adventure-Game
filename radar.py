from mobile import *
from room import *


class Radar (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc, desc)

    def use (self,actor):
        def names (lst):
            return ', '.join([x.name() for x in lst])
        actor.say('I fiddle with the buttons on ' + actor.name());
        for loc in Room.rooms:
            people = self.people_around(loc, actor)
            all_stuff = self.stuff_around(loc)
            if all_stuff:
                actor.say('I detect '+ names(all_stuff)+ ' in '+ loc.name())
            if people:
                actor.say('I detect '+ names(people)+ ' in '+ loc.name())
                    
    def people_around (self, location, actor):
        return [x for x in location.contents() if x.is_person() and x is not actor]

    def stuff_around (self, location):
        return [x for x in location.contents() if not x.is_person()]
