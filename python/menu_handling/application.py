"""Implements Application class."""

class Application():
    """Implements Application class methods."""
    def __init__(self):
        """Initialize instance."""
        pass

    def split_string(self):
        input_string = input('Enter sentence or phrase: ')
        # Split input string on spaces (default)
        input_list = input_string.split()
        separator_string = input('Enter separator string: ')

        for s in input_list:
            print(f'{s}{separator_string}', end='')

        print()

        print(f'len(input_list) = {len(input_list)}')

        for i in range(len(input_list)):
            print(f'{i}:{input_list[i][0]}{separator_string}', end='')

    def create_list(self):
        names = []
        names.append('Rick')
        names.append('Jawaher')
        names.append('Matthew')
        names.append('Joseph')
        names.append('Davis')
        names.append('Lewis')
        names.append('Bader')
        names.append('Anthony')
        names.append('Aysha')
        names.append('Shatha')
        names.append('Theresa')

        for name in names:
            print(f'{name} - ', end='')

        print()

        names.sort()

        for name in names:
            print(f'{name} - ', end='')



