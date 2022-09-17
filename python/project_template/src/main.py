# Explicit main execution module

from example import Example

'''
main() function
'''
def main():
	example = Example()
	print(f'Count = { example.get_count() }')
	example.iter_demo()
	example.lambda_demo();


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()