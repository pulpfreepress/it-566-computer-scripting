# Class Example

class Example:
	"""
		Doc comments...
		Example class
	"""

	def __init__(self):
		self.count = 0


	def get_count(self):
		return self.count


	def increment_count(self):
		self.count += 1
		return self.count 


	def sum(self, arg_a, arg_b):
		return arg_a + arg_b


	def iter_demo(self):
		message = 'A string of letters is also a list of chars...'
		for s in message:
			print(f'{s} ', end="")
		print()


	def lambda_demo(self):
		print(f'{list(map(lambda x: x + x , [1,2,3,4,5] ))} ', end="")




