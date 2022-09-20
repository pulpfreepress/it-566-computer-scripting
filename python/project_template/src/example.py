"""example module contains Example class."""

class Example:
	"""Doc comments.
	
	Example class
	"""

	def __init__(self):
		"""Initialize example object."""
		self.count = 0


	def get_count(self):
		"""Return self.count."""
		return self.count


	def increment_count(self):
		"""Increment and return self.count."""
		self.count += 1
		return self.count 


	def sum(self, arg_a, arg_b):
		"""Return sum of arg_a + arg_b."""
		return arg_a + arg_b


	def iter_demo(self):
		"""Demonstrate string iteration."""
		message = 'A string of letters is also a list of chars...'
		for s in message:
			print(f'{s} ', end="")
		print()


	def lambda_demo(self):
		"""Demonstrate lambda function."""
		print(f'{list(map(lambda x: x + x , [1,2,3,4,5] ))} ', end="")




