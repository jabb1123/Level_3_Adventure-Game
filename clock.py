
class Clock (object):

    def __init__ (self,_time):
        self._time = _time
        self.regfunc = {}
    
    def time(self):
        return self._time
    
    def set_time(self,_time):
        self._time = _time
    
    def tick(self):
        self._time += 1
    
    def print_tick_action(self):
        print "The clock chimes "+ str(self._time)
    
    def register(self, func_name, priority, target):
        if priority not in self.regfunc.keys():
            func_list = []
            func_list.append((func_name,target))
            self.regfunc[priority] = func_list
            
        else:
            previous_funcs = self.regfunc[priority]
            previous_funcs.append((func_name,target))
            self.regfunc[priority] = previous_funcs
    
    def unregister(self,func_name,priority,target):
        if priority not in self.regfunc.keys():
            return
        else:
            previous_funcs = self.regfunc[priority]
            previous_funcs.remove((func_name,target))
            self.regfunc[priority] = previous_funcs
            
    def call_regfunc(self,time):
        for key in self.regfunc.keys():
            for func in self.regfunc[key]:
                if func[1] == None:
                    func[0]()
                else:
                    func[0](time)