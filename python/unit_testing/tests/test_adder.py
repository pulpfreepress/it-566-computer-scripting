"""Test Adder class methods."""

import pytest
from context import Adder

class Test_Example:

	def test_adder(self):
		adder = Adder()
		assert adder.add(2, 2) == 4
		assert adder.add(2.3, 2.2) == 4.5
		


	
