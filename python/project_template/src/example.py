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





def main():
	example = Example()
	print(f'Count = { example.get_count() }')

if __name__ == '__main__':
	main()

