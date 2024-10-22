"""Demonstrate Writing and Reading Text to a File."""

import os

def main():
    greeting = 'Hello World!'
    print(f'Working Dir: {os.getcwd()}')

    working_dir = os.getcwd()
    data_dir = 'data'
    file_name = 'greeting.txt'
    data_dir_path = os.path.join(working_dir, data_dir)

    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)


    try:
        with open(os.path.join(data_dir_path, file_name), 'w') as f:
            f.write(greeting)
            




    except (OSError, Exception) as e:
        print(f'Problem with file I/O: {e}')

if __name__ == '__main__':
    main()