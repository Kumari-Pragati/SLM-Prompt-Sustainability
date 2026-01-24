import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4, 5]), 3.0)

    def test_single_number(self):
        self.assertEqual(multiply_num([5]), 5)

    def test_zero_number(self):
        self.assertEqual(multiply_num([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(multiply_num([-1, -2, -3]), -2.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(multiply_num([10**6, 10**6]), 10**6)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(multiply_num([1.5, 2.5]), 3.75)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(multiply_num([1, 2.5, -3]), -1.5)
