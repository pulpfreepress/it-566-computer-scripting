"""Explicit main execution module."""

import curses
from curses import wrapper
from curses.textpad import rectangle
from example import Example
import time


def main(stdscr):
	"""Execute main program."""
	stdscr.clear()
	stdscr.addstr(0, 0, '-' * 80, curses.COLOR_BLUE)
	for i in range(60):
		stdscr.clear()
		stdscr.addstr(10, i, 'Hello World!', curses.A_BLINK)
		stdscr.refresh()
		time.sleep(.1)
	
	rectangle(stdscr, 2, 2, 10, 20)
	stdscr.addstr(11, 2, 'This is a rectangle! ')
	stdscr.refresh()
	stdscr.getch()
	
	


# Call main() if this is the main execution module
if __name__ == '__main__':
	wrapper(main)