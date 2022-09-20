"""Explicit main execution module."""
from inventory_app import InventoryApp




def main():
	"""Execute when it's the main execution module."""
	home_inventory_app = InventoryApp()
	home_inventory_app.start_application()


	
	


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()