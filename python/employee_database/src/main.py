"""Main entry point for Employee Database."""

from person import Person

def main()->None:
    """Main entry point."""
    p1 = Person(first_name='Rick', last_name='Miller')

    print(f'{p1}')


if __name__ == '__main__':
    main()