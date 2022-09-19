"""example Module.

Contains one class named Example which defines
various methods demonstrating this or that.
"""

"""Example class.

Example class contains various methods that demonstrate various
topics. Example class will change over time.
"""
class Example:
	"""This is a summary line.
	
	The summary line starts immediately following the three double quotes.
	The summary line ends in a period followed by one blank line.
	"""

	def __init__(self):
		"""Initialize Example object.
		
		Instance variables:
		- self.count -- Integer 
		"""
		self.count = 0


	def get_count(self):
		"""Return value of self.count."""
		return self.count


	def increment_count(self):
		"""Add 1 to self.count and return."""
		self.count += 1
		return self.count 


	def sum(self, arg_a, arg_b):
		"""Add two integer arguments and return the sum."""
		return arg_a + arg_b


	def iter_demo(self):
		"""Demonstrate interation over characters in a string."""
		message = 'A string of letters is also a list of chars...'
		for s in message:
			print(f'{s} ', end="")

		print()


	def lambda_demo(self):
		"""Demonstate lambda function definition and map() function."""
		print(f'{list(map(lambda x: x + x , [1,2,3,4,5] ))} ', end="")


	def list_operations(self):
		"""Demonstrate operations on lists."""
		print(f'{min([1,2,3,4,5])}')
		print(f'{1 in [1,2,3,4,5]}')
		list_of_ints = [1,2,3,4,5]
		list_of_ints.append(6)
		print(f'{6 in list_of_ints}')
		print(f'{len(list_of_ints)}')
		print(f'{[1,2,3,4,5,6][0]}')
		print(f'{"Hello, World!"[0]}')





