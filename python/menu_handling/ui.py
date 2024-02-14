"""Provides User Interface services."""

from application import Application

class Ui:
    """Defines user interface methods."""

    def __init__(self):
        """Called when instance of class is created."""
        self._keep_going = True
        self._application = Application()

    def display_menu(self):
        print('\n')
        print('\t\tApplication Menu\n')
        print('\t\t1. Demo Lists')
        print('\t\t2. Demo Dictionaries')
        print('\t\t6. Exit')
        print('\n')
        
    def process_menu_choice(self):
        user_input = input('\t\tPlease enter menu choice: ')
        #print(f'You entered {user_input[0]}')

        match user_input[0]:
            case '1': self.demo_lists()
            case '2': self.demo_dictionaries()
            case '6': self._keep_going = False
            case _: print('Invalid choice!')

    def start(self):
        while(self._keep_going):
            self.display_menu()
            self.process_menu_choice()


    def demo_lists(self):
        #self._application.split_string()
        self._application.create_list()


    def demo_dictionaries(self):
        print('demo_dictionaries() called...')



