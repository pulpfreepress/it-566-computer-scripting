import json


class Person():

    def __init__(self, firstName: str, middleName: str, lastName: str):
        if not isinstance(firstName, str):
            raise Exception('Arguments must be strings.')
        self.first_name = firstName
        self.middle_name = middleName
        self.last_name = lastName

    def __str__(self):
        return self.to_json()
    
    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
    
    
    
    


class PersonJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return o.__dict__

    

    
