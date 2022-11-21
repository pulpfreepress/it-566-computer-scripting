"""Implements household roster control features."""

from roster import Roster
from subprocess import call
import os

class RosterApp(object):
	"""Implements household roster control features."""

	def __init__(self):
		"""Initialize object."""
		# Constants
		self.NEW_ROSTER='1'
		self.LOAD_ROSTER='2'
		self.PRINT_ROSTER='3'
		self.ADD_MEMBERS='4'
		self.SAVE_ROSTER='5'
		self.EXIT='7'
		# Fields
		self.menu_choice = 1
		self.keep_going = True
		self.team_roster = Roster()
		pass

	def clear_screen(self):
		os.system('clear')

	def display_menu(self):
		"""Display menu."""
		print('\t\t\tTeam Roster Application')
		print()
		print('\t\t1. New Roster')
		print('\t\t2. Load Roster')
		print('\t\t3. Print Roster')
		print('\t\t4. Add Team Members to Roster')
		print('\t\t5. Save Roster')
		print('\t\t7. Exit')
		print()

	def process_menu_choice(self):
		"""Process menu choice and execute corrensponding methods."""
		self.menu_choice = input('Please enter menu item number: ')
		if __debug__:
			print(f'You entered: {self.menu_choice}')
		match self.menu_choice:
			case self.NEW_ROSTER:
				self.new_roster()
			case self.LOAD_ROSTER:
				self.load_roster()
			case self.PRINT_ROSTER:
				self.print_roster()
			case self.ADD_MEMBERS:
				self.add_members()
			case self.SAVE_ROSTER:
				self.save_roster()
			case self.EXIT:
				if __debug__:
					print('Goodbye!')
				self.keep_going = False
				self.clear_screen()
			case _:
				self.clear_screen()
				print('Invalid Menu Choice!')

	def new_roster(self):
		"""Create new roster."""
		self.clear_screen()
		if __debug__:
			print('new_roster() method called...')

	def load_roster(self):
		"""Load roster from file."""
		self.clear_screen()
		if __debug__:
			print('load_roster() method called...')


	def print_roster(self):
		"""Print roster."""
		self.clear_screen()
		if __debug__:
			print('print_roster() method called...')
		


	def save_roster(self):
		"""Save roster to file."""
		self.clear_screen()
		if __debug__:
			print('save_roster() method called...')
		


	def add_members(self):
		"""Add items to roster."""
		self.clear_screen()
		if __debug__:
			print('print_roster() method called...')




	def start_application(self):
		"""Start the applications."""
		# Clear Screen
		self.clear_screen()
		while self.keep_going:
			self.display_menu()
			self.process_menu_choice()
