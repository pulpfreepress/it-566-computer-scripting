# Command-Line Argument Processing

Demonstrates how to process command line arguments using the argparse module. 

## Architecture
- Two modules: 
```
src/example.py
src/main.py
```

## Operation
- `./build.sh --runmain`  Runs the program
- I pass the arguments to the program in the bash script's runmain() method. 


## Modifications
If you want to experiment with different arguments you can do several things.
- Modify the arguments in the bash script's runmain() method, or
- Modify the bash script to pass the arguments from the command line to the runmain() method, or
- You can run the python program directly from the command line with pipenv like so: `pipenv run python3 src/main.py [arguments]`

## Unit Tests
The main module contains a separate parse_args() method to facilitate testing. Refer to the tests/test_main.py file.

## References
Solution to enable testing command line arguments came from Stack Overflow: https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module

Code for argparse demo came straight from the Python docs: https://docs.python.org/3/library/argparse.html

