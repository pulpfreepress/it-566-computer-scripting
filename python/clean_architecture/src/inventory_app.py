"""Implements inventory application presentation layer (U/I) features."""

from business_logic import BusinessLogic
from prettytable import PrettyTable
import os

class InventoryApp(object):
	"""Implements household inventory control features."""

	def __init__(self):
		"""Initialize object."""
		# Constants
		self.NEW_INVENTORY='1'
		self.LIST_INVENTORIES='2'
		self.SELECT_INVENTORY='3'
		self.LIST_INVENTORY_ITEMS='4'
		self.ADD_ITEMS='5'
		self.EXIT='6'
		# Fields
		self.menu_choice = 1
		self.keep_going = True
		self.business_logic = BusinessLogic()
		self.active_inventory_id = 0

	def clear_screen(self):
		try:
			os.system('clear')
		except Exception:
			os.system('cls')

	def display_menu(self):
		"""Display menu."""
		print('\t\t\tHousehold Inventory Application')
		print()
		print('\t\t1. New Inventory')
		print('\t\t2. List Inventories')
		print('\t\t3. Select Inventory')
		print('\t\t4. List Inventory Items')
		print('\t\t5. Add Items')
		print('\t\t6. Exit')
		print()

	def process_menu_choice(self):
		"""Process menu choice and execute corrensponding methods."""
		self.menu_choice = input('Please enter menu item number: ')
		if __debug__: 
			print(f'You entered: {self.menu_choice}')
		match self.menu_choice:
			case self.NEW_INVENTORY:
				self.new_inventory()
			case self.LIST_INVENTORIES:
				self.list_inventories()
			case self.SELECT_INVENTORY:
				self.select_inventory()
			case self.LIST_INVENTORY_ITEMS:
				self.list_inventory_items()
			case self.ADD_ITEMS:
				self.add_items()
			case self.EXIT:
				if __debug__:
					print('Goodbye!')
				self.keep_going = False
				self.clear_screen
			case _:
				print('Invalid Menu Choice!')

	def new_inventory(self):
		"""Create new inventory."""		
		if __debug__:
			print('new_inventory() method called...')
		

	def list_inventories(self):
		"""List inventories."""
		if __debug__:
			print('list_inventories() method called...')
			self.clear_screen()
			self.print_inventory_list(self.get_inventories())
			input('\n\nPress any key to continue...')
			

	def get_inventories(self):
		return self.business_logic.get_all_inventories()


		
	def select_inventory(self):
		"""Selects an existing inventory"""
		if __debug__:
			print('select_inventory() method called.')
		self.print_inventory_list(self.get_inventories())
		self.active_inventory_id = int(input('\n\nSelect inventory id from list: '))
		


	def list_inventory_items(self):
		"""List inventory."""
		if __debug__:
			print('list_inventory_items() method called...')
		items_list = self.business_logic.get_items_for_inventory_id(self.active_inventory_id)
		self.print_items_list(items_list)
		input('\n\nPress any key to continue...')
		

	def add_items(self):
		"""Add items to inventory."""
		if __debug__:
			print('add_items() method called...')
		# to do


	def start_application(self):
		"""Start the applications."""
		while self.keep_going:
			self.clear_screen()
			self.display_menu()
			self.process_menu_choice()
			
					
	def print_inventory_list(self, inv_list):
		t = PrettyTable(['ID', 'Name', 'Description'])
		for row in inv_list:
			t.add_row([row[0], row[1], row[2]])
		print(t)

	def print_items_list(self, items_list):
		t = PrettyTable(['ID', 'Inventory ID', 'Item', 'Count'])
		for row in items_list:
			t.add_row([row[0], row[1], row[2], row[3]])
		print(t)



		

