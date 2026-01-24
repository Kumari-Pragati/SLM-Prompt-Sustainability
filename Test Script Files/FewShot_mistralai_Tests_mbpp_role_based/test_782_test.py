import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOdd_Length_Sum(unittest.TestCase):
    def test_positive_odd_length(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 32)

    def test_positive_even_length(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 10)

    def test_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3]), -18)

    def test_zero_in_list(self):
        self.assertEqual(Odd_Length_Sum([0, 1, 2, 3]), 10)
