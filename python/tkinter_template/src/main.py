"""Explicit main execution module."""

from example import Example
from tkinter import *
from tkinter import ttk



def main():
	"""Execute main program."""
	root = Tk()
	frm = ttk.Frame(root, padding=10)
	frm.grid()
	ttk.Label(frm, text='Hello World!').grid(column=0, row=0)
	ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)
	root.mainloop()


# Call main() if this is the main execution module
if __name__ == '__main__':
	main()