# Explicit main execution module
import sys
import argparse
from example import Example


'''
parse_args() function.
Separate to enable testing with pytest
The code for this example comes straight from the Python docs:
https://docs.python.org/3/library/argparse.html

The solution to test command line arguments came from Stack Overflow:
https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module

'''
def parse_args(args):
	parser = argparse.ArgumentParser(description='Demonstrate how to pass command-line arguments to a Python program.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='An integer for the accumulator')
	parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='Sum the integers (default: find the max)')
	return parser.parse_args(args)


'''
main() function
'''
def main(cmd_line_args):
	example = Example()
	args = parse_args(cmd_line_args)
	print(args.accumulate(args.integers))


# Call main() if this is the main execution module
if __name__ == '__main__':
	main(sys.argv[1:])