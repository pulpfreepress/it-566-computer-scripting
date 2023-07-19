from person import Person
import json


class Student(Person):

    def __init__(self, firstName: str, middleName: str, lastName: str, studentId: str, major: str):
        # Constructor chaining
        super().__init__(firstName, middleName, lastName)
        # Then set derived class properties
        self.student_id = studentId
        self.major = major

    def __str__(self):
        return self.to_json()
    
    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)
    

class StudentJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Student):
            return o.__dict__

    