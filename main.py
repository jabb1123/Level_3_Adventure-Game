
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

    radar1= Radar('handy-radar',mh353, 'Can look at everything.') 
    radar2= Radar('handy-radar',oval, 'Can look at everything.') 
    thing1= Thing('blackboard', ac113, 'You can write stuff on it')
    thing2= Thing('lovely-trees', oval, 'It looks pretty lovely.')
    thing3= Thing('track', bGym, 'You can run on it.')
    
    mob1= MobileThing('Weights',bGym,'Very heavy. Can throw at enemies.')
    mob2= MobileThing('Nerf Gun',westh, 'Can shoot and kill people.')
    npc1= NPC('Babo',bHealth,random.randint(1,5),random.randint(1,5),'Aggresive type')
    npc2= NPC('Gabe-the-Babie',babson,random.randint(1,5),random.randint(1,5), 'Submissive type.')
    
    
    mob3=MobileThing('cs-book', oval, 'Learn computer stuff.')
    mob4=MobileThing('math-book', oval, 'Learn math stuff.')

    comp1= Computer('Laptop', oval, "Android 1")
    comp2= Computer('computer', easth, "Android 2")
    hw0= Homework('hw-0',oval,'it is')
                 
    prof1= Professor('Superman', oval,3,2,"superguy.")
    prof2= Professor('Riccardo',mh353,random.randint(1,5),2, 'The cool type.')
    
    hw1 = Homework('hw-1',random.choice(Room.rooms),"I'm due at midnight!")
    hw2 = Homework('hw-2',random.choice(Room.rooms),"I'm due at midnight!")
    hw3 = Homework('hw-3',random.choice(Room.rooms),"I'm due at midnight!")
    hw4 = Homework('hw-4',random.choice(Room.rooms),"I'm due at midnight!")
    hw5 = Homework('hw-5',random.choice(Room.rooms),"I'm due at midnight!")
    hw6 = Homework('hw-6',random.choice(Room.rooms),"I'm due at midnight!")

    stud1= NPC('Frankie Freshman',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")
    stud2= NPC('Joe Junior',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")
    stud3= NPC('Sophie Sophomore',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")
    stud4= NPC('Cedric Senior',random.choice(Room.rooms),random.randint(1,5),random.randint(1,5), "I came to learn")

    troll1 = Troll('Polyphemus',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    troll2 = Troll('Jack',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    troll3 = Troll('Beast',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    troll4 = Troll('Red',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    troll5 = Troll('Black',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")
    troll6 = Troll('Atterns',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I'll eat your face!")

    trollhunt1= TrollHunter('Killer',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    trollhunt2= TrollHunter('Hunter',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    trollhunt3= TrollHunter('Death',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    trollhunt4= TrollHunter('Van',random.choice(Room.rooms),random.randint(1,3),random.randint(1,3),"I kill them trolls!")
    
    cat1 = Caterpillar(0,'Stinger', oval, "He's such a cute little bug!")
    
    def Store_reg_elements():
        current_time = Player.clock.time()
        Player.clock.register(Player.clock.tick,1,None)
        Player.clock.register(Player.clock.print_tick_action,1,None)
        Player.clock.register(Player.me.look_around,1,None)
        
        Player.clock.register(troll1.move_and_take_stuff,1,current_time)
        Player.clock.register(troll2.move_and_take_stuff,1,current_time)
        Player.clock.register(troll3.move_and_take_stuff,1,current_time)
        Player.clock.register(troll4.move_and_take_stuff,1,current_time)
        Player.clock.register(troll5.move_and_take_stuff,1,current_time)
        Player.clock.register(troll6.move_and_take_stuff,1,current_time)
        Player.clock.register(trollhunt1.move_and_take_stuff,2,current_time)
        Player.clock.register(trollhunt2.move_and_take_stuff,2,current_time)
        Player.clock.register(trollhunt3.move_and_take_stuff,2,current_time)
        Player.clock.register(trollhunt4.move_and_take_stuff,2,current_time)
        Player.clock.register(prof1.move_and_take_stuff,1,current_time)
        Player.clock.register(prof2.move_and_take_stuff,1,current_time)
        Player.clock.register(stud1.move_and_take_stuff,1,current_time)
        Player.clock.register(stud2.move_and_take_stuff,1,current_time)
        Player.clock.register(stud3.move_and_take_stuff,1,current_time)
        Player.clock.register(stud4.move_and_take_stuff,1,current_time)
        Player.clock.register(cat1.new_age,1,current_time)
        
        Player.clock.register(troll1.eat_people,2,current_time)
        Player.clock.register(troll2.eat_people,2,current_time)
        Player.clock.register(troll3.eat_people,2,current_time)
        Player.clock.register(troll4.eat_people,2,current_time)
        Player.clock.register(troll5.eat_people,2,current_time)
        Player.clock.register(troll6.eat_people,2,current_time)
        Player.clock.register(prof1.lecture,2,current_time)
        Player.clock.register(prof2.lecture,2,current_time)
        Player.clock.register(trollhunt1.kill_trolls,1,current_time)
        Player.clock.register(trollhunt2.kill_trolls,1,current_time)
        Player.clock.register(trollhunt3.kill_trolls,1,current_time)
        Player.clock.register(trollhunt4.kill_trolls,1,current_time)
        Player.clock.register(cat1.transform,2,None)
        

        
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

        else:
            print 'What??'
            

if __name__ == '__main__':
    main()
