    # define getter and setters
class Role():
    def __init__(self, name = None):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self):
        self.__name = "First-Line Supervisors of Production and Operating Workers"