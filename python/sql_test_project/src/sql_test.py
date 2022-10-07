"""Demonstrates creating a database connection and inserting and reading data."""

from mysql.connector import connect, Error

class SqlTest:
	"""Demo class to connect, insert, and query data from a database."""

	def __init__(self, db_host, db_port, db_name, db_user_name, db_password):
		self._db_port = db_port
		self._db_name = db_name
		self._db_host = db_host
		self._db_user_name = db_user_name
		self._db_password = db_password
		self.db_connection = None

	def insert_item(self, item_name, item_count):
		try:
			with connect(
				host=self._db_host,
				user=self._db_user_name,
				password=self._db_password,
				database=self._db_name,
				port=self._db_port
			) as connection:
				print(connection)
		except Error as e:
			print(e)


