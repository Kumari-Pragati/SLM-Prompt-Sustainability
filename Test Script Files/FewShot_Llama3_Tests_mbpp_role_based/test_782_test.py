import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOdd_Length_Sum(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_single_element_array(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_even_length_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 10)

    def test_odd_length_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(Odd_Length_Sum([1, -2, 3, -4]), 0)
