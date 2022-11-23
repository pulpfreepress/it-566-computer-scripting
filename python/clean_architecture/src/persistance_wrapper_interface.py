"""Specifies persistance wrapper interface methods."""

from abc import ABC, abstractmethod

class PersistanceWrapperInterface(ABC):
	"""Specifies persistance wrapper interface methods."""

	def __init__(self, persistance_type: str):
		self._persistance_type = str(persistance_type)

	@abstractmethod
	def get_all_inventories(self):
		pass

	@abstractmethod
	def get_items_for_inventory(self, inventory_id: int):
		pass

	@abstractmethod
	def create_inventory(self, name: str, description: str, date: str):
		pass

	@abstractmethod
	def create_item(self, inventory_id: int, item: str, count: int):
		pass
