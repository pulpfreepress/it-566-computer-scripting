"""Implements Home Inventory data structures and operations."""

import json
from datetime import date

class HomeInventory():
    """Implements Home Inventory data structures and operations."""

    def __init__(self):
        """Initialize Home Inventory object."""
        self.dictionary = {} # Initialize to empty dictionary
        self._initialize_home_inventory_dictionary()
        
    def new_inventory(self):
        """Initialize new dictionary to store inventory data."""
        if (self.dictionary != None) and (bool(self.dictionary)):
            user_input = input("Safe current inventory? (y/n): ")
            match user_input.lower():
                case 'y':
                    self.save_inventory()
                    self._initialize_home_inventory_dictionary()
                case 'n':
                    self._initialize_home_inventory_dictionary()
                case _:
                    self._initialize_home_inventory_dictionary()
        else:
            self._initialize_home_inventory_dictionary()

    def load_inventory(self):
        """Load inventory from file."""
        if __debug__:
            print('load_inventory() method called...')
        try:
            file_path = self._get_file_path()
            with open(file_path, 'r', encoding='UTF-8') as f:
                self.dictionary = json.loads(f.read())
        except OSError:
            print('Problem loading file. Please try again.')

    def save_inventory(self):
        """Save inventory to file."""
        if __debug__:
            print('save_inventory() method called...')
        if self.dictionary != None:
            file_path = self._get_file_path()
            with open(file_path, 'w', encoding='UTF-8') as f:
                f.write(json.dumps(self.dictionary))

    def add_item(self, item_name, item_count):
        assert self.dictionary != None
        self.dictionary['items'].append({'item': item_name, 'count': int(item_count)})

    def list_inventory(self):
        """List inventory to console."""
        if __debug__:
            print('list_inventory() method called..')
        for key, value in self.dictionary.items():
            if key == 'items':
                print('items:')
                for item in value:
                    print(f'\t {item["item"]:10} \t {item["count"]}')
            else:
                print(f'{key}: \t {value}')

    def _get_file_path(self):
        """Get flle path from user."""
        f_path = input("Please enter path and filename: ")
        return f_path

    def _list_inventory_files(self):
        """List all files in directory with _inventory.json file suffix."""
        if __debug__:
            print('_list_inventory_files() method called...')

    def _initialize_home_inventory_dictionary(self):
        if __debug__:
            print("Initializing new Home Inventory...")
        self.dictionary = {}
        self.dictionary['type'] = 'Home Inventory'
        self.dictionary['date'] = date.today().isoformat()
        self.dictionary['items'] = []
        if __debug__:
            print("New Home Inventory Initialized")



