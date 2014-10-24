Level_3_Adventure-Game
======================
OlinLand
by Jacob Riedel and Julian Morris

Special attributes
-Player's name is self
-Dragon burns all people in one area 
-People can pick up weapons and armour
-Player can attack other people
-Babo detains people and takes them to Babson Public Safety

Feedback
-It was not difficult, but lots of debugging when making modification to one part of the code.
-The modularization made the entiIt was not difficult, but lots of debugging when making modification to one part of the code.re implementation a much better learning experience for me.
-Stacking the classes to create one final hierarchy was really interesting.

Extensions

Dragon class, Babo class, and weaponandarmor class were created.
Also implemented an attack method for player. NPC’s and players can now be attacked, and players can attack.



 

 

DEMO OF WEAPONS

 

You are in Oval
The Oval, smack in the center of Olin College.
You see: handy-radar, lovely-trees, Stinger, ShortSword, leather-armor
You see: Superman, stealth
Exits: west, east, north, south


Events:


What is thy bidding? look self
self
Hey! That's me!
Strength: 5
Health: 5/5

 

What is thy bidding? take ShortSword
self says -- I took ShortSword

 

What is thy bidding? take leather-armor
self says -- I took leather-armor

 

What is thy bidding? look self
self
Hey! That's me!
ShortSword, leather-armor
Strength: 8
Health: 10/10

 

What is thy bidding? attack Superman
Superman says -- SHREEEEEK! I, uh, suddenly feel very faint...
An earth-shattering, soul-piercing scream is heard...
Superman has been slain...


DEMO OF DRAGON

 

------------------------------------------------------------

You are in Oval
The Oval, smack in the center of Olin College.
You see: handy-radar, lovely-trees, hw-1, Stinger, ShortSword, Rocket-Launcher, leather-armor, Fire-Proof-suit
You see: Superman, Jack, stealth, stealth, Smaug
Exits: west, east, north, south


Events:


What is thy bidding? look self
self
Hey! That's me!
Strength: 5
Health: 5/5
 

What is thy bidding? take Rocket-Launcher
self says -- I took Rocket-Launcher

 
What is thy bidding? take Fire-Proof-suit
self says -- I took Fire-Proof-suit

 

What is thy bidding? attack Smaug
Smaug says -- How dare you slay me!! AAAAAHHHHHHHHHHHHHH!!!!!!
You have slain the dragon. You gain the dragon sword and the dragon shield.
Smaug has been slain...
Jack says -- I try to take handy-radar but can't
An earth-shattering, soul-piercing scream is heard...
Van says -- Hi self, Superman, Jack, stealth, stealth
The clock chimes 1
Jack takes a bite out of self
self says -- Ouch! 3 hits is more than I want!
self says -- My health is now 102
stealth says -- I took hw-1
stealth says -- Burn all homework!!.
hw-1 was destroyed.

------------------------------------------------------------

You are in Oval
The Oval, smack in the center of Olin College.
You see: handy-radar, lovely-trees, Stinger, ShortSword, leather-armor, Dragon-Sword, Dragon-Shield
You see: Superman, Jack, stealth, stealth, Van
Exits: west, east, north, south

 
Events:

 
What is thy bidding? take Dragon-Sword
self says -- I took Dragon-Sword

 
What is thy bidding? take Dragon-Shield
self says -- I took Dragon-Shield

 
What is thy bidding? look self
self
Hey! That's me!
Rocket-Launcher, Fire-Proof-suit, Dragon-Sword, Dragon-Shield
Strength: 155
Health: 302/305

 
What is thy bidding? look Dragon-Sword
Dragon-Sword
The most powerful sword in the game. Burns everyone. +100 Str

 
 
DEMO OF BABO

 

------------------------------------------------------------

You are in Oval
The Oval, smack in the center of Olin College.
You see: handy-radar, lovely-trees, Stinger, ShortSword, leather-armor
You see: Dot-the-Dalmatian
Exits: west, east, north, south

Events:


What is thy bidding? wait
Dot-the-Dalmatian says -- I try to take handy-radar but can't
An earth-shattering, soul-piercing scream is heard...
An earth-shattering, soul-piercing scream is heard...
An earth-shattering, soul-piercing scream is heard...
An earth-shattering, soul-piercing scream is heard...
------------------------------------------------------------
You are in Oval
The Oval, smack in the center of Olin College.
You see: handy-radar, lovely-trees, Stinger, ShortSword, leather-armor
You see: Dot-the-Dalmatian
Exits: west, east, north, south

Events:



What is thy bidding? wait
Dot-the-Dalmatian says -- I try to take leather-armor but can't
The clock chimes 1
Dot-the-Dalmatian arrests self
self says -- I'm to pretty to go to jail!
Dot-the-Dalmatian says -- Too bad! Crime always pays!
------------------------------------------------------------
You are in Babson-Public-Saftey
Beware the criminal, some of them bite!.
The room is empty
You see: Peter-Po-Po, Dot-the-Dalmatian
Exits: south

Events:



What is thy bidding? 