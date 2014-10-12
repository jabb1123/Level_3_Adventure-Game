from mobile import *
from room import *


class Radar (MobileThing):

    def __init__ (self,name,loc,description):
        MobileThing.__init__(self,name,loc)
        self.description = description

    def use (self,actor):
        actor.say('I fiddle with the buttons on ' + self.name());
        # FIX ME
        actor.say("Mmm. It looks like it's broken...")
