import pytest
from context import main

class Test_Main:

	def test_sum(self):
		args = main.parse_args(['1','2','3','4','5'])
		assert args.accumulate(args.integers) == 5

	def test_max(self):
		args = main.parse_args(['1','2','3','4','5', '--sum'])
		assert args.accumulate(args.integers) == 15


	

		



