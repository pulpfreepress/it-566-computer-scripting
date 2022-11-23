"""Serves as user interface"""

from business_logic import BusinessLogic

class HomeInventoryApp(object):
	
	def __init__(self):
		self._business_logic = BusinessLogic()

	def create_inventory(self, name: str, description: str, date: str):
		self._business_logic.create_new_inventory(name, description, date)

	def get_all_inventories(self):
		return self._business_logic.get_all_inventories()

	def get_all_inventories_with_format(self, format):
		return self._business_logic.get_all_inventories_with_format(format)