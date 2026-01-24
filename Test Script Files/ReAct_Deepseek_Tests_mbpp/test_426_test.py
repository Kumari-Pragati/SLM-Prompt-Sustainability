import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(filter_oddnumbers([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(filter_oddnumbers([2, 4, 6, 8]), [])

    def test_negative_numbers(self):
        self.assertEqual(filter_oddnumbers([-1, -2, -3, -4]), [-1, -3])

    def test_mixed_positive_negative(self):
        self.assertEqual(filter_oddnumbers([-1, 2, -3, 4, 5]), [-1, -3, 5])

    def test_large_numbers(self):
        self.assertEqual(filter_oddnumbers([100, 200, 301, 402]), [301])

    def test_duplicates(self):
        self.assertEqual(filter_oddnumbers([1, 1, 2, 3, 3, 4, 5]), [1, 3, 5])
