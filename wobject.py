
class WObject (object):
    def __init__ (self,n,desc):
        self._name = n.replace(' ', '-')
        self._desc = desc

    def name (self):
        return self._name
        
    def describe(self):
        return self._desc
      
    def is_thing (self):
        return False
  
    def is_mobile_thing (self):
        return False

    def is_person (self):
        return False

    def is_room (self):
        return False

    def is_homework (self):
        return False
