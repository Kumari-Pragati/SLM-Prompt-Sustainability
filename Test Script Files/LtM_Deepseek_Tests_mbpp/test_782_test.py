import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3]), 6)

    def test_empty_input(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_single_element_input(self):
        self.assertEqual(Odd_Length_Sum([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3]), -6)

    def test_large_numbers(self):
        self.assertEqual(Odd_Length_Sum([1000, 2000, 3000]), 6000)

    def test_mixed_numbers(self):
        self.assertEqual(Odd_Length_Sum([1, -2, 3, -4]), 4)

    def test_odd_length_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 15)

    def test_even_length_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 9)
