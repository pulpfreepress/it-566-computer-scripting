"""Explicit main execution module."""
from home_inventory_app import HomeInventoryApp
from datetime import date

def main():
	"""Execute main program."""
	app = HomeInventoryApp()
	#app.create_inventory('Garage', 'Stuff in the garage.', date.today().isoformat())
	print(app.get_all_inventories())
	print('-' * 25)
	print(app.get_all_inventories_with_format('json'))

	


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()
