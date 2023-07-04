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
        return super().__str__() + " " + self.student_id \
        + " " + self.major
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    