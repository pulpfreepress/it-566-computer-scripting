"""Explicit main execution module."""

from getpass import getpass
from sql_test import SqlTest


def main():
	"""Execute main program."""
	#password = getpass('Enter DB Password: ')
	password = None
	db_test = SqlTest('localhost', 3306, 'home_inventory', 'home_inventory_user', password)
	item = input("Item name: ")
	count = input("Item count: ")
	db_test.insert_item(item, int(count))
	print(db_test.query_all())


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()
