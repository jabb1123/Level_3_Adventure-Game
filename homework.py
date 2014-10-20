from mobile import *


class Homework (MobileThing):

    def __init__ (self,name,loc,desc):
        MobileThing.__init__(self,name,loc,desc)
        self.done = False

    def is_homework (self):
        return True
    
    def is_done_homework (self):
        self.done = True

   
    def check_done_homework(self):
        return self.done


