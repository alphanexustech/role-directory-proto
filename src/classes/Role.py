    # define getter and setters
class Role():
    def __init__(self, name = None):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, x):
        self.__name = x

test_role_01 = Role()
test_role_01.set_name("First-Line Supervisors of Production and Operating Workers")

test_role_02 = Role()
test_role_02.set_name("Another Role")

roles = [test_role_01, test_role_02]

for r in roles:
    print(r.get_name())