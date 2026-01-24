import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOdd_Length_Sum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_single_element_array(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_even_length_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 6)

    def test_odd_length_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([1, -2, 3, -4, 5]), 3)

    def test_zero_in_array(self):
        self.assertEqual(Odd_Length_Sum([0, 1, 2, 3, 4, 5]), 15)
