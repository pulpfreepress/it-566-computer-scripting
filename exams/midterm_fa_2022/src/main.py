"""Explicit main execution module."""

from roster_app import RosterApp



def main():
	"""Execute when it's the main execution module."""
	roster_app = RosterApp()
	roster_app.start_application()
	

	


	
# Call main() if this is the main execution module
if __name__ == '__main__':
	main()