from player import *
from npc import *

class Dragon(NPC):
    def __init__ (self,name,loc,restlessness,_rage, desc):
        Person.__init__(self,name,loc, desc)
        self._max_health = 50
        self._health = self._max_health
        self.restlessness = restlessness
        self._rage = 2
        Player.clock.register(self.burn_everything,1,Player.clock.time)
        Player.clock.register(self.move_somewhere,1,Player.clock.time)
    

    def burn_everything (self,time):
      if not self.is_in_limbo():
        if random.randrange(self._rage) == 0:
            people = self.people_around()
            for people in self.people_around():
                self.location().report(self.name() + ' burns ' + victim.name())
                victim.suffer(10)
            else:
                self.location().report(self.name() + " is ready to burn things.")
    
    def move_somewhere (self):
        exits = self.location().exits()
        if exits:
            dir = random.choice(exits.keys())
            self.go(dir)
    
    def is_dragon(self):
        return True

    def die (self):
        self.say('How dare you slay me!! AAAAAHHHHHHHHHHHHHH!!!!!!')
        Player.clock.unregister(self.burn_everything,1,Player.clock.time)
        Player.clock.unregister(self.move_somewhere,1,Player.clock.time)
        self.destroy()
        print "You have slain the dragon. You gain the dragon sword and the dragon shield."
        DragonSword = WeaponAndArmor("Dragon Sword",Player.me.location(),"The most powerful sword in the game. Burns everyone. +100 Str",100,0)
        DragonShield = WeapnAndArmor("Dragon Shield", Player.me.location(), "The most powerful shield in the game. You are invincible. +200 Def",0,200 )
        Player.me.contents().append(DragonSword)
        Player.me.contents().append(DragonShield)
