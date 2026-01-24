import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddnumbers(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_empty_input(self):
        self.assertEqual(filter_oddnumbers([]), [])

    def test_all_even_input(self):
        self.assertEqual(filter_oddnumbers([2, 4, 6, 8]), [])

    def test_negative_numbers(self):
        self.assertEqual(filter_oddnumbers([-1, -2, -3, -4]), [-1, -3])

    def test_large_numbers(self):
        self.assertEqual(filter_oddnumbers(list(range(1, 1001))), list(range(1, 1001, 2)))
