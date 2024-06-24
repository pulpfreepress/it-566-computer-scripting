"""Demonstrate Writing and Reading Text to a File."""

import os

def main():
    greeting = 'Hello World!'
    print(f'Working Dir: {os.getcwd()}')

    try:
        with open('greeting.txt', 'w') as f:
            f.write(greeting)


    except (OSError, Exception) as e:
        print(f'Problem with file I/O: {e}')

if __name__ == '__main__':
    main()