''' Author: 	Your Name
	Project:	Project Name
	Date:		Date
'''

import string


''' A function that takes one argument 
	named message whose default value is
	set to the value 'Hello, World!'
'''
def main(message='Hello, World!'):
	print(message)

	s = ''
	while s != 'q':
		s = input('Enter a message or "q" to exit: ')
		print(s)




''' If this file is being directly executed 
	by python then its __name__ attribute will
	be set to the string '__main__' indicating
	it's the main module. If so, run the main
	function.
'''


if __name__ == '__main__':
	main()

