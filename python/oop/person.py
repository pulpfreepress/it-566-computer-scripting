import json

class Person:

    def __init__(self, firstName: str, middleName: str, lastName: str):
        if not isinstance(firstName, str):
            raise Exception('Arguments must be strings.')
        self.first_name = firstName
        self.middle_name = middleName
        self.last_name = lastName

    def __str__(self):
        return str(self.first_name) + ' ' + \
        str(self.middle_name[0]) + '. ' + str(self.last_name)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    

    

    
