"""Demonstrates creating a database connection and inserting and reading data."""

from mysql.connector import connect, Error

class SqlTest:
	"""Demo class to connect, insert, and query data from a database."""

	def __init__(self, db_host, db_port, db_name, db_user_name, db_password):
		"""Initialize object properties."""
		# Fields
		self._db_port = db_port
		self._db_name = db_name
		self._db_host = db_host
		self._db_user_name = db_user_name
		self._db_password = db_password
		self.db_connection = None

		# Constants
		self.SELECT_ALL = 'SELECT id, item, count FROM items'
		self.INSERT = 'INSERT INTO items (item, count) VALUES(%s, %s)'


	def insert_item(self, item, count):
		try:
			with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
				cursor = connection.cursor()
				cursor.execute(self.INSERT, (item, count))
				connection.commit() # Very important!
				cursor.close()


		except Error as e:
			print(e)


	def query_all(self):
		results = None
		try:
			with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
				cursor = connection.cursor()
				cursor.execute(self.SELECT_ALL)
				results = cursor.fetchall()

		except Error as e:
			print(e)

		return results


