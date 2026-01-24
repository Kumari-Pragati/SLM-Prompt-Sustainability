import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_input(self):
        self.assertListEqual(filter_oddnumbers([]), [])

    def test_single_input(self):
        self.assertListEqual(filter_oddnumbers([1]), [1])

    def test_negative_numbers(self):
        self.assertListEqual(filter_oddnumbers([-1, -2, -3]), [-1, -3])

    def test_max_value(self):
        self.assertListEqual(filter_oddnumbers(range(2**31 - 1)), range(1, 2**31 - 1, 2))

    def test_min_value(self):
        self.assertListEqual(filter_oddnumbers(range(-2**31 + 1)), range(-2**31 + 1, 0, 2))
