from mobile import *
from player import *

class Person (MobileThing):    # Container...

    def __init__ (self,name,loc, desc):
        MobileThing.__init__(self,name,loc,desc)
        self._max_health = 3
        self._health = self._max_health
        self._contents = []
        

    def health (self):
        return self._health

    def reset_health (self):
        self._health = self._maxHealth

    def say (self,msg):
        loc = self.location()
        loc.report(self.name()+' says -- '+msg)

    def have_fit (self):
        self.say('Yaaaaah! I am upset!')

    def people_around (self):
        return [x for x in self.location().contents() 
        if x.is_person() and x is not self]
                        
    def professors_around (self):
        return [x for x in self.location().contents() 
        if x.is_professor() and x is not self]
                        
    def trolls_around (self):
        return [x for x in self.location().contents() 
        if x.is_troll() and x is not self]

    def stuff_around (self):
        return [x for x in self.location().contents() if not x.is_person()]


    # this function should return everything that everyone in the
    # same location as this person are holding/carrying

    def peek_around (self):
        everyItem = []
        for person in self.people_around():
            for item in person.contents():
                everyItem.append(item)
        return everyItem

    def lose (self,t,loseto):
        self.say('I lose ' + t.name())
        self.have_fit()
        t.move(loseto)
    
    def go (self,direction):
        loc = self.location()
        exits = loc.exits()
        if direction in exits:
            t = exits[direction]
            self.leave_room()
            loc.report(self.name()+' moves from '+ loc.name()+' to '+t.name())
            self.move(t)
            self.enter_room()
            return True
        else:
            print 'No exit in direction', direction
            return False


    def suffer (self,hits):
        self.say('Ouch! '+str(hits)+' hits is more than I want!')
        self._health -= hits
        if (self.health() < 0):
            self.die()
        else:
            self.say('My health is now '+str(self.health()))


    def detain(self,cop,loc):
        self.say("I'm to pretty to go to jail!")
        cop.say("Too bad! Crime always pays!")
        loc.add_thing(self)
        loc.add_thing(cop)
        self._location = loc
        cop._location = loc
        
    
    
    def die (self):
        self.location().broadcast('An earth-shattering, soul-piercing scream is heard...')
        self.destroy()
        

    def enter_room (self):
        people = self.people_around()
        if people:
            self.say('Hi ' + ', '.join([x.name() for x in people]))

    def leave_room (self):
        pass   # do nothing to reduce verbiage

    def take (self,actor):
        actor.say('I am not strong enough to just take '+self.name())
        

    def drop (self,actor):
        print actor.name(),'is not carrying',self.name()

    def give (self,actor,target):
        print actor.name(),'is not carrying',self.name()
        
    def accept (self,obj,source):
        self.say('Thanks, ' + source.name())

    def is_person (self):
        return True
        
    def add_thing (self,t):
        self._contents.append(t)

    def del_thing (self,t):
        self._contents = [x for x in self._contents if x is not t]
    
    def have_thing(self,thing):
        for i in self.contents():
            if i==thing:
                return True
        return False
        
    def contents(self):
        return [x for x in self._contents]

