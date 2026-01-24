import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_even_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 10)

    def test_odd_length_list_with_zero(self):
        self.assertEqual(Odd_Length_Sum([0, 1, 2, 3, 4]), 15)

    def test_large_list(self):
        self.assertEqual(Odd_Length_Sum(list(range(100))), 27499)
