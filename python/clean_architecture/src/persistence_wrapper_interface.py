"""Specifies persistence wrapper interface methods."""

from abc import ABC, abstractmethod

class PersistenceWrapperInterface(ABC):
	"""Specifies persistance wrapper interface methods."""

	def __init__(self, persistance_type: str):
		self._persistance_type = str(persistance_type)

	@abstractmethod
	def get_all_inventories(self):
		"""Returns a list of inventories."""
		pass

	@abstractmethod
	def get_items_for_inventory(self, inventory_id: int):
		"""Returns a list of inventory items for given inventory id."""
		pass

	@abstractmethod
	def create_inventory(self, name: str, description: str, date: str):
		"""Inserts a new inventory into the datastore."""
		pass

	@abstractmethod
	def create_item(self, inventory_id: int, item: str, count: int):
		"""Inserts new item into datastore for given inventory id."""
		pass
