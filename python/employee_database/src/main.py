"""Main entry point for Employee Database."""

from person import Person
from employee import Employee

def main()->None:
    """Main entry point."""
    p1 = Person(first_name='Rick', last_name='Miller')
    print(f'{p1}')

    e1 = Employee('Rick', 'Miller', '0001', 'Janitor')
    print(f'{e1}')

    


if __name__ == '__main__':
    main()