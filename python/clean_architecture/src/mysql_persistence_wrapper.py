"""Implements a MySQL Persistence Wrapper"""

from persistence_wrapper_interface import PersistenceWrapperInterface
from mysql import connector

class MySQLPersistenceWrapper(PersistenceWrapperInterface):
	"""Implements MySQL Persistance Wrapper"""

	def __init__(self):
		# Constants
		self.SELECT_ALL_INVENTORIES = 'SELECT id, name, description FROM inventories'
		self.INSERT = 'INSERT INTO items (inventory_id, item, count) VALUES(%s, %s, %s)'
		self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID = 'SELECT id, inventory_id, item, count FROM items WHERE inventory_id = %s'
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = 'home_inventory'
		self.DB_CONFIG['user'] = 'home_inventory_user'
		self.DB_CONFIG['host'] = '127.0.0.1'
		self.DB_CONFIG['port'] = 8889 

		self._db_connection = self._initialize_database_connection(self.DB_CONFIG)

	def get_all_inventories(self):
		cursor = None
		try:
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_INVENTORIES)
			results = cursor.fetchall()

		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		
		return results

	def get_items_for_inventory(self, inventory_id):
		cursor = None
		try:
			cursor = self._db_connection.cursor()
			cursor.execute(self.SELECT_ALL_ITEMS_FOR_INVENTORY_ID, ([inventory_id]))
			results = cursor.fetchall()

		except Exception as e:
			print(f'Exception in persistance wrapper: {e}')
		
		return results

	def create_inventory(self, name: str, description: str, date: str):
		pass

	def create_item(self, inventory_id: int, item: str, count: int):
		pass
		
		
	def _initialize_database_connection(self, config):
		cnx = None
		try:
			cnx = connector.connect(pool_name = 'dbpool', pool_size=10, **config)
		
		except Exception as e:
			print(e)

		return cnx



