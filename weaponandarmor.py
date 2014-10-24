# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 21:18:52 2014

@author: jmorris
"""

from mobile import *

class WeaponAndArmor(MobileThing):
    def __init__ (self,name,loc,desc,attack,defense):
        MobileThing.__init__(self,name,loc,desc)
        self.attack = attack
        self.defense = defense
    
    def is_weaponandarmor(self):
        return True
    
    def is_player(self):
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    