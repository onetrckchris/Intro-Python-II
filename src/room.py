class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{repr(self.name)}"
    
    def check_direction(self, direction):
        if self.__getattribute__(direction) != None:
            return self.__getattribute__(direction)
        else:
            return 'N/A'
