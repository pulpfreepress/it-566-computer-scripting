"""Defines Person class and related properties and operations."""

class Person:
    """Defines Person class."""

    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name

    """
    def __str__(self)->str:
        return f'{self.first_name} {self.last_name}'
    
    def __repr__(self)->str:
        return self.__str__()
    """

    
