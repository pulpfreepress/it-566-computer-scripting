"""Implements household inventory control features."""

import sys

class InventoryApp():
	"""Implements household inventory control features."""


	def __init__(self):
		# Constants
		self.NEW_INVENTORY='1'
		self.LOAD_INVENTORY='2'
		self.LIST_INVENTORY='3'
		self.EXIT='7'
		# Fields
		self.menu_choice = 1
		self.keep_going = True
		pass

	def display_menu(self):
		print('\t\t\tHousehold Inventory Application')
		print()
		print('\t\t1. New Inventory')
		print('\t\t2. Load Inventory')
		print('\t\t3. List Inventory')
		print('\t\t7. Exit')
		print()

	def process_menu_choice(self):
		self.menu_choice = input('Please enter menu item number:')
		print(f'You entered: {self.menu_choice}')
		match self.menu_choice:
			case self.NEW_INVENTORY:
				self.new_inventory()
			case self.LOAD_INVENTORY:
				self.load_inventory()
			case self.LIST_INVENTORY:
				self.list_inventory()
			case self.EXIT:
				print('Goodbye!')
				self.keep_going = False
			case _:
				print('Invalid Menu Choice!')

	def new_inventory(self):
		print('new_inventory() method called...')

	def load_inventory(self):
		print('load_inventory() method called...')

	def list_inventory(self):
		print('list_inventory() method called...')

	def start_application(self):
		while self.keep_going:
			self.display_menu()
			self.process_menu_choice()
			
					



		


