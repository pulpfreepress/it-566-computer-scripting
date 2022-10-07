"""Represent application user interface."""

class InventoryApp:
    
    def __init__(self):
        # Constants
        self.NEW_INVENTORY = '1'
        self.LOAD_INVENTORY = '2'
        self.SAVE_INVENTORY = '3'
        self.EXIT = '7'

        self.keep_going = True

    def display_menu(self):
        print()
        print('\tHome Inventory Application')
        print()
        print('\t\t1. New Inventory')
        print('\t\t2. Load Inventory')
        print('\t\t3. Save Inventory')
        print('\t\t7. Exit')
        print()

    def process_menu_choice(self):
        menu_choice = input('Select Menu Item Number: ')
        if __debug__:
            print(menu_choice[0])
        match menu_choice[0]:
            case self.NEW_INVENTORY:
                self.new_inventory()
            case self.EXIT:
                self.keep_going = False
            case _:
                print('Bad, bad user...')


    def new_inventory(self):
        if __debug__:
            print('new_inventory() method called...')

    def load_inventory(self):
        if __debug__:
            print('load_inventory() method called...')

    def save_inventory(self):
        if __debug__:
            print ('save_inventory() method called...')

    def start_program(self):
        while self.keep_going:
            self.display_menu()
            self.process_menu_choice()