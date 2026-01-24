import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(filter_oddnumbers([]), [])

    def test_single_even_number(self):
        self.assertListEqual(filter_oddnumbers([2]), [])

    def test_single_odd_number(self):
        self.assertListEqual(filter_oddnumbers([1]), [1])

    def test_mixed_numbers(self):
        self.assertListEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_negative_numbers(self):
        self.assertListEqual(filter_oddnumbers([-1, -2, -3]), [-1])

    def test_large_numbers(self):
        self.assertListEqual(filter_oddnumbers(list(range(100, 1000, 2))), list(range(100, 1000, 2)))
