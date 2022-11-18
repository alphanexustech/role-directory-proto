    # define getter and setters
class Role():
    def __init__(self, employment = None, name = None):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, x):
        self.__name = x
    
    def get_employment(self):
        return self.__employment

    def set_employment(self, x):
        self.__employment = x

    def get_mean_hourly_wage(self):
        return self.__mean_hourly_wage

    def set_mean_hourly_wage(self, x):
        self.__mean_hourly_wage = x
    
    def get_mean_annual_wage(self):
        return self.__mean_annual_wage

    def set_mean_annual_wage(self, x):
        self.__mean_annual_wage = x

test_role_01 = Role()
test_role_01.set_name("First-Line Supervisors of Production and Operating Workers")


test_role_02 = Role()
test_role_02.set_name("Hello")

roles = [test_role_01, test_role_02]

i = 0
for r in roles:
    i += 1
    print("Role " + str(i))
    print(r.get_name())    