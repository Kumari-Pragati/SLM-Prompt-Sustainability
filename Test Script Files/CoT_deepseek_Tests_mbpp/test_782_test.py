import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 45)

    def test_single_element(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_empty_list(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5]), -5)

    def test_large_numbers(self):
        self.assertEqual(Odd_Length_Sum([1000, 2000, 3000, 4000, 5000]), 9265000)

    def test_duplicate_elements(self):
        self.assertEqual(Odd_Length_Sum([1, 1, 1, 1, 1]), 5)

    def test_float_elements(self):
        self.assertAlmostEqual(Odd_Length_Sum([1.5, 2.5, 3.5, 4.5, 5.5]), 17.5)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum([1, 2, '3', 4, 5])

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            Odd_Length_Sum([1, 2, None, 4, 5])
