import json


def main():
	aliases = ['Rick', 'Hey You!', 'Butt Face', 'Mr. Smith']
	person = {}
	person['firstName'] = 'Richard'
	person['lastName'] = 'Miller'
	person['aliases'] = aliases
    
	print(json.dumps(person, indent=4))
    

if __name__ == '__main__':
    main()