"""Serves as entry point for project."""

from adder import Adder

def main():
    """Entry point function for project."""
    adder = Adder()
    print(adder.add(2,2))

if __name__ == '__main__':
    main()