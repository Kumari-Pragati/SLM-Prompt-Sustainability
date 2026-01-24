import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_even_length_list(self):
        self.assertEqual(Odd_Length_Sum([1, 2]), 1)
        self.assertEqual(Odd_Length_Sum([1, 2, 3]), 6)
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4]), 10)

    def test_odd_length_list_with_zero(self):
        self.assertEqual(Odd_Length_Sum([0, 1, 2]), 3)
        self.assertEqual(Odd_Length_Sum([0, 1, 2, 3]), 11)
        self.assertEqual(Odd_Length_Sum([0, 1, 2, 3, 4]), 19)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([1, -2, 3]), 8)
        self.assertEqual(Odd_Length_Sum([-1, -2, 3]), -2)
        self.assertEqual(Odd_Length_Sum([-1, -2, -3]), -6)

    def test_large_numbers(self):
        self.assertEqual(Odd_Length_Sum([1000000001, 1000000002, 1000000003]), 500000003)

    def test_invalid_input(self):
        self.assertRaises(TypeError, Odd_Length_Sum, 1.5)
        self.assertRaises(TypeError, Odd_Length_Sum, ("string"))
