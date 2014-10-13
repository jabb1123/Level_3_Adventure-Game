
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

    Player('Blubbering-Fool', oval, "Hey! That's me!")

    Radar('handy radar',mh353, 'Can look at everything.') 
    Radar('handy radar',oval, 'Can look at everything.') 
    Thing('blackboard', ac113, 'You can write stuff on it')
    Thing('lovely-trees', oval, 'It looks pretty lovely.')
    
    MobileThing('Weights',bGym,'Very heavy. Can throw at enemies.')
    MobileThing('Nerf Gun',westh, 'Can shoot and kill people.')
    NPC('Babo',bHealth,random.randint(1,5),random.randint(1,5),'Aggresive type')
    NPC('Gabe-the-Babie',babson,random.randint(1,5),random.randint(1,5), 'Submissive type.')
    Thing('track', bGym, 'You can run on it.')
    
    MobileThing('cs-book', oval, 'Learn computer stuff.')
    MobileThing('math-book', oval, 'Learn math stuff.')

    Computer('hal-9000', ac113, "Android 1")
    Computer('johnny-5', easth, "Android 2")

    Professor('Riccardo',mh353,random.randint(1,5),2, 'The cool type.')
    
    homeworks = ['hw-1', 
                 'hw-2',
                 'hw-3',
                 'hw-4',
                 'hw-5',
                 'hw-6']
    
    for homework in homeworks:
        Homework(homework,
                 random.choice(Room.rooms),
                 "I'm due at midnight!")

    students = ['Frankie Freshman',
                'Joe Junior',
                'Sophie Sophomore',
                'Cedric Senior']

    for student in students:
        NPC(student,
            random.choice(Room.rooms),
            random.randint(1,5),
            random.randint(1,5),
            "I came to learn")

    trolls = ['Polyphemus',
              'Gollum']

    for troll in trolls:
      Troll(troll,
            random.choice(Room.rooms),
            random.randint(1,3),
            random.randint(1,3),
            "I'll eat your face!")


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
    
    Player.me.look_around()

    while True:
        response = read_player_input ()
        print
        if response[0] in VERBS:
            result = VERBS[response[0]].act(response[1:])
            if result == NEXT_ROUND:
                Player.me.look_around()
        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
