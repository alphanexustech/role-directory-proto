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
    
    def get_percentile_10(self):
        return self.__percentile_10
    # x is hourly wage percentile, y is anual wage percentile
    def set_percentile_10(self, x, y):
        self.__percentile_10 = [x, y]
    
    def get_percentile_25(self):
        return self.__percentile_25
    # x is hourly wage percentile, y is anual wage percentile
    def set_percentile_25(self, x, y):
        self.__percentile_25 = [x, y]

    def get_percentile_50(self):
        return self.__percentile_50
    # x is hourly wage percentile, y is anual wage percentile
    def set_percentile_50(self, x, y):
        self.__percentile_50 = [x, y]

    def get_percentile_75(self):
        return self.__percentile_75
    # x is hourly wage percentile, y is anual wage percentile
    def set_percentile_75(self, x, y):
        self.__percentile_75 = [x, y]

    def get_percentile_90(self):
        return self.__percentile_90
    # x is hourly wage percentile, y is anual wage percentile
    def set_percentile_90(self, x, y):
        self.__percentile_90 = [x, y]
    
    def get_industry_highest_level_employment(self):
        return self.__industry_highest_level_employment

    def set_industry_highest_level_employment(self, x, y, z):
        self.__industry_highest_level_employment = [x, y, z]
    
    def get_industry_highest_concentration_employment(self):
        return self.__industry_highest_concentration_employment

    def set_industry_highest_concentration_employment(self, x, y, z):
        self.__industry_highest_concentration_employment = [x, y, z]

    def get_industry_top_paying_industries(self):
        return self.__industry_top_paying_industries

    def set_industry_top_paying_industries(self, x, y, z):
        self.__industry_top_paying_industries = [x, y, z]
    
    def get_state_highest_level_employment(self):
        return self.__state_highest_level_employment

    def set_state_highest_level_employment(self, x, y, z):
        self.__state_highest_level_employment = [x, y, z]

    def get_state_highest_concentration_employment(self):
        return self.__state_highest_concentration_employment

    def set_state_highest_concentration_employment(self, x, y, z):
        self.__state_highest_concentration_employment = [x, y, z]
    
    def get_state_top_paying(self):
        return self.__state_top_paying

    def set_state_top_paying(self, x, y, z):
        self.__state_top_paying = [x, y, z]

    def get_metropolitan_highest_level_employment(self):
        return self.__metropolitan_highest_level_employment

    def set_metropolitan_highest_level_employment(self, x, y, z):
        self.__metropolitan_highest_level_employment = [x, y, z]

    def get_metropolitan_highest_concentration_employment(self):
        return self.__metropolitan_highest_concentration_employment

    def set_metropolitan_highest_concentration_employment(self, x, y, z):
        self.__metropolitan_highest_concentration_employment = [x, y, z]
    
    def get_metropolitan_top_paying(self):
        return self.__metropolitan_top_paying

    def set_metropolitan_top_paying(self, x, y, z):
        self.__metropolitan_top_paying = [x, y, z]

    def get_non_metropolitan_highest_level_employment(self):
        return self.__non_metropolitan_highest_level_employment

    def set_non_metropolitan_highest_level_employment(self, x, y, z):
        self.__non_metropolitan_highest_level_employment = [x, y, z]

    def get_non_metropolitan_highest_concentration_employment(self):
        return self.__non_metropolitan_highest_concentration_employment

    def set_non_metropolitan_highest_concentration_employment(self, x, y, z):
        self.__non_metropolitan_highest_concentration_employment = [x, y, z]
    
    def get_non_metropolitan_top_paying(self):
        return self.__non_metropolitan_top_paying

    def set_non_metropolitan_top_paying(self, x, y, z):
        self.__non_metropolitan_top_paying = [x, y, z]

test_role_01 = Role()
test_role_01.set_name("First-Line Supervisors of Production and Operating Workers")
test_role_01.set_percentile_10(123, 456)

test_role_02 = Role()
test_role_02.set_name("Hello")
test_role_02.set_percentile_10(124, 568)

roles = [test_role_01, test_role_02]

i = 0
for r in roles:
    i += 1
    print("Role " + str(i))
    print(r.get_name())
    print(r.get_percentile_10())