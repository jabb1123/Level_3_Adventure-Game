
import random

from room import *
from verbs import *
from player import *
from npc import *
from radar import *
from troll import *
from professor import *
from homework import *
from computer import *
from trollhunter import *
from caterpillar import *
from badninja import *
from dragon import *
from weaponandarmor import *



REVERSE = {
    'north' : 'south',
    'east' : 'west',
    'south' : 'north',
    'west' : 'east',
    'up' : 'down',
    'down' : 'up'
}


# add an exit in 'fr' toward 'to' in direction 'dir'
def connect (fr,dir,to):
    fr.exits()[dir] = to

# add an exit in 'fr' toward 'to' in direction 'dir'
# and an exit the other way, in 'to' toward 'fr' in the reverse direction
def biconnect (fr,dir,to):
    connect(fr,dir,to)
    connect(to,REVERSE[dir],fr)



def create_world ():

    mh353 = Room('Riccardo Office','')
    mh3rd = Room('Milas Hall Third Floor','')
    mh2nd = Room('Milas Hall Second Floor','')
    mh1st = Room('Milas Hall First Floor','Where admissions is')
    oval = Room('Oval', 'The Oval, smack in the center of Olin College.')
    ac1st = Room('Academic Center First Floor','Machine shop and a couple of classrooms.')
    ac113 = Room('Academic Center 113','Game Programming classroom.')
    cc1st = Room('Campus Center First Floor','Where Oliners eat.')
    westh = Room('West Hall','Where underclassman live.')
    easth = Room('East Hall','Where upper classman live.')
    babson = Room('Babson College','Where the babos are.')
    
    bTrim = Room('Trim dinning hall','Where the babos eat.')
    bHealth = Room('Babson Public Health','Where everyone goes to be healthy.')
    bGym = Room('Babson Gym','Where you go to get fit.')
    cc2nd = Room('Campus Center Second Floor', 'The crescent room')
    cc3rd = Room('Campus Center Third Floor', 'A Mystery.')

    biconnect(mh353, 'east',  mh3rd)
    biconnect(mh3rd, 'down',  mh2nd)
    biconnect(mh2nd, 'down',  mh1st)
    biconnect(mh1st, 'north',  oval)
    biconnect(oval, 'east',  cc1st)
    biconnect(cc1st, 'east',  westh)
    biconnect(westh, 'east',  easth)
    biconnect(oval, 'north',  babson)
    biconnect(oval, 'west',  ac1st)
    biconnect(ac1st, 'north',  ac113)
    
    biconnect(babson,'north', bTrim)
    biconnect(babson,'west', bHealth)
    biconnect(babson,'east', bGym)
    biconnect(cc2nd, 'down', cc1st)
    biconnect(cc3rd, 'down', cc2nd)
    

    # The player is the first 'thing' that has to be created

    Player('self', oval, "Hey! That's me!")
    Radar('handy-radar',mh353, 'Can look at everything.') 
    Radar('handy-radar',oval, 'Can look at everything.') 
    Thing('blackboard', ac113, 'You can write stuff on it')
    Thing('lovely-trees', oval, 'It looks pretty lovely.')
    Thing('track', bGym, 'You can run on it.')
    
    MobileThing('Weights',bGym,'Very heavy. Can throw at enemies.')
    MobileThing('Nerf Gun',westh, 'Can shoot and kill people.')
    NPC('Babo',bHealth,random.randint(1,5),random.randint(1,5),'Aggresive type')
    NPC('Gabe-the-Babie',babson,random.randint(1,5),random.randint(1,5), 'Submissive type.')
    
    
    MobileThing('cs-book', oval, 'Learn computer stuff.')
    MobileThing('math-book', oval, 'Learn math stuff.')

    Computer('Laptop', oval, "Android 1")
    Computer('computer', easth, "Android 2")
    Homework('hw-0',oval,'it is')
                 
    Professor('Superman', oval,3,2,"superguy.")
    Professor('Riccardo',mh353,random.randint(1,5),2, 'The cool type.')
    
    Homework('hw-1',random.choice(Room.rooms),"I'm due at midnight!")
    Homework('hw-2',random.choice(Room.rooms),"I'm due at midnight!")
    Homework('hw-3',random.choice(Room.rooms),"I'm due at midnight!")
    Homework('hw-4',random.choice(Room.rooms),"I'm due at midnight!")
    Homework('hw-5',random.choice(Room.rooms),"I'm due at midnight!")
    Homework('hw-6',random.choice(Room.rooms),"I'm due at midnight!")

    NPC('Frankie Freshman',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")
    NPC('Joe Junior',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")
    NPC('Sophie Sophomore',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")
    NPC('Cedric Senior',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")

    Troll('Polyphemus',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    Troll('Jack',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    Troll('Beast',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    Troll('Red',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    Troll('Black',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    Troll('Atterns',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")

    TrollHunter('Killer',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    TrollHunter('Hunter',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    TrollHunter('Death',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    TrollHunter('Van',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    
    Caterpillar(0,'Stinger', oval, "He's such a cute little bug!")
    
    BadNinja('stealth',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"Burn them Homeworks!")
    BadNinja('stealth',oval,random.randint(1,3),random.randint(1,3),"Burn them Homeworks!")
    BadNinja('stealth',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"Burn them Homeworks!")
    
    dragon1 = Dragon('Smaug',random.choice(Room.rooms),random.randint(1,3),random.randint(1,2),"Most powerful enemy. Known to burn everything when angry. You need the Dragon shield to protect yourself from it." )

    weapon1 = WeaponAndArmor("ShortSword",oval,"Weakest weapon. Strong enough to kill trolls in one blow. +3 str",3,0)
    weapon2 = WeaponAndArmor("LongSword",random.choice(Room.rooms),"fairly strong weapon. Strong enough to kill badNinjas in one blow. +5 str",5,0)
    weapon3 = WeaponAndArmor("Katana",random.choice(Room.rooms),"A very powerful weapon. You now have a fighting chance against a dragon, but not really.",10,0)
    weapon4 = WeaponAndArmor("Rocket Launcher",mh353,"A cheat weapon. Strong enough to kill anyone in one blow.",50,0)
    armor1 = WeaponAndArmor("leather armor",oval,"Weakest armor. Strong enough to withstand troll bites a little. +3 def",0,5)
    armor2 = WeaponAndArmor("steel armor",random.choice(Room.rooms),"fairly strong armor. Strong enough to withstand troll bites for a while. +5 def",0,5)
    armor3 = WeaponAndArmor("golden armor",random.choice(Room.rooms),"A very powerful armor. You now have a fighting chance against a dragon, but not really. +20 def",0,20)
    armor4 = WeaponAndArmor("Fire Proof suit",mh353,"A cheat armor. Strong enough to withstand anything.",0,100)
    
    def Store_reg_elements():
        current_time = Player.clock.time()
        Player.clock.register(Player.clock.tick,1,None)
        Player.clock.register(Player.clock.print_tick_action,1,None)
        Player.clock.register(Player.me.look_around,3,None)        
    Store_reg_elements()
VERBS = {
    'quit' : Quit(),
    'look' : Look(),
    'wait' : Wait(),
    'take' : Take(),
    'drop' : Drop(),
    'give' : Give(),
    'god'  : God(),
    'use'  : Use(),
    'north' : Direction('north'),
    'south' : Direction('south'),
    'east' : Direction('east'),
    'west' : Direction('west'),
    'up'   : Direction('up'),
    'down' : Direction('down')
    #,'check': Check()
}
  

def print_tick_action (t):
    Player.me.location().report('The clock ticks '+str(t))


def read_player_input ():
    while True:
        response = raw_input('\nWhat is thy bidding? ')
        if len(response)>0:
            return response.split()
    
    
SAME_ROUND = 1
NEXT_ROUND = 2  
  
def main ():
    
    print 'Olinland, version 1.4 (Fall 2014)\n'


    # Create the world
    create_world()
    
    #Store_reg_elements()
    Player.me.look_around()

    while True:
        response = read_player_input ()
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.clock.call_regfunc(Player.clock.time())
                print 
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
