import unittest

from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5]), 40)

    def test_empty_array(self):
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_single_element_array(self):
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_two_element_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2]), 4)

    def test_odd_length_array(self):
        self.assertEqual(Odd_Length_Sum([1, 2, 3, 4, 5, 6]), 56)

    def test_negative_numbers(self):
        self.assertEqual(Odd_Length_Sum([-1, -2, -3, -4, -5]), -10)

    def test_large_numbers(self):
        self.assertEqual(Odd_Length_Sum([100, 200, 300, 400, 500]), 92700)

    def test_float_numbers(self):
        self.assertAlmostEqual(Odd_Length_Sum([1.5, 2.5, 3.5, 4.5, 5.5]), 18.5)
