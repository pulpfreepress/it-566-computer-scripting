"""Defines Employee Class."""

from person import Person

class Employee(Person):
    """Defines Employee Class."""

    def __init__(self, first_name:str, last_name:str, \
                 employee_no:str, position:str):
        super().__init__(first_name, last_name)
        self.employee_number = employee_no
        self.position = position

    def __str__(self)->str:
        #return f'{super().__str__()} {self.position} {self.employee_number}'
        return f'{self.first_name} {self.last_name} {self.position} {self.employee_number}'

    def __repr__(self)->str:
        return self.__str__()