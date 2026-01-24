import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddnumbers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_oddnumbers([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(filter_oddnumbers([2, 4, 6, 8]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(filter_oddnumbers([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_mixed_numbers(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_single_number(self):
        self.assertEqual(filter_oddnumbers([5]), [5])

    def test_negative_numbers(self):
        self.assertEqual(filter_oddnumbers([-1, -3, -5, 2, 4]), [-1, -3, -5])
