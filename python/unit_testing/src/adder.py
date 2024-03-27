"""Demonstrate unit testing."""
from numbers import Number

class Adder():
    """Defines methods to add stuff."""

    def __init__(self):
        """Initialize object instance."""
        pass

    def add(self, a:Number, b:Number) -> Number:
        if not isinstance(a, Number ):
            raise Exception("Invalid value for parameter a.")
        if not isinstance(b, Number):
            raise Exception("Invalid value for parameter b.")
        
        return a + b
    
    def sub(self, a:Number, b:Number) -> Number:
        pass

        