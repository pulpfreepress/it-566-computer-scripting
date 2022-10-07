"""Explicit main execution module."""
from inventory_app import InventoryApp

def main():
	"""Execute main program."""
	inventory_app = InventoryApp()
	inventory_app.start_program()


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()