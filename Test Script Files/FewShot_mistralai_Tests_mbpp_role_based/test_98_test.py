import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4]), 1.5)

    def test_zero_in_list(self):
        self.assertAlmostEqual(multiply_num([1, 0, 3, 4]), 1.3333333333333333)

    def test_empty_list(self):
        self.assertEqual(multiply_num([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(multiply_num([-1, -2, -3, -4]), -3.0)

    def test_single_number(self):
        self.assertAlmostEqual(multiply_num([5]), 5.0)
