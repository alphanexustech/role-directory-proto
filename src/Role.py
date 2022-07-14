from pprint import pprint

# Role model
class Role:
    def __init__(self, name, description, bls_id, keywords):
        self.name = name
        self.description = description
        self.bls_id = bls_id
        self.keywords = keywords
    
    def get_role(self):
        return self.__dict__

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_bls_id(self):
        return self.bls_id

    def get_keywords(self):
        return self.keywords



name = 'Plumber'
description = 'A plumber improves buildings by controlling the water flow through pipes'
bls_id = '10-000000'
keywords = ['pipe', 'water', 'improve', 'building']


# Test area for experimenting with role

r = Role(name, description, bls_id, keywords)
print(r.get_name(), r.get_description(), r.get_bls_id(), r.get_keywords())