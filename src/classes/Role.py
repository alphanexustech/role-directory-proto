    # define getter and setters
class Role():
    def __init__(self, name = None):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, x):
        self.__name = x

first_line_supervisors_of_roduction_and_operating_workers = Role

first_line_supervisors_of_roduction_and_operating_workers.set__name("First-Line Supervisors of Production and Operating Workers")

print(first_line_supervisors_of_roduction_and_operating_workers.get__name())

print(first_line_supervisors_of_roduction_and_operating_workers.__name)