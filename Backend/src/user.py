
class User:
    def __init__(self):
        self.name = {}
        
    def add_user(self, firstName, lastName):
        self.name[firstName.strip()] = lastName.strip()
        return 'Successfully added'

    def get_user(self, name):
        if name not in self.name.keys():
            return False, None    
        userData = {"firstName": name, "lastName": self.name[name]}
        return True, userData
        
        
