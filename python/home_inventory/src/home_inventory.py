"""Implements Home Inventory data structures and operations."""

from contextlib import nullcontext
import sys
import string
import json



class HomeInventory():
    """Implements Home Inventory data structures and operations."""

    def __init__(self):
        """Initialize Home Inventory object."""
        self.dictionary = None



    def new_inventory(self):
        """Initialize new dictionary to store inventory data."""
        if self.dictionary != None:
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
        print('load_inventory() method called...')

    def save_inventory(self):
        """Save inventory to file."""
        print('save_inventory() method called...')
        if self.dictionary != None:
            file_path = self._get_file_path()
            with open(file_path, 'w', encoding='UTF-8') as f:
                f.write(json.dumps(self.dictionary))

    def add_item(self, item_name, item_count):
        assert self.dictionary != None
        self.dictionary[item_name] = item_count

    def list_inventory(self):
        """List inventory to console."""
        print('list_inventory() method called..')

    def _get_file_path(self):
        """Get flle path from user."""
        f_path = input("Please enter path and filename: ")
        return f_path

    def _list_inventory_files(self):
        """List all files in directory with _inventory.json file suffix."""
        print('_list_inventory_files() method called...')

    def _initialize_home_inventory_dictionary(self):
        print("Initializing new Home Inventory...")
        self.dictionary = {}
        print("New Home Inventory Initialized")



