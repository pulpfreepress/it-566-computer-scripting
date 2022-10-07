"""Explicit main execution module."""

from getpass import getpass
from sql_test import SqlTest


def main():
	"""Execute main program."""
	password = getpass('Enter DB Password: ')
	db_test = SqlTest('localhost', 8889, 'home_inventory', 'home_inventory_user', password)
	db_test.insert_item('Truck', 1)


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()