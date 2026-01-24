import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4]), 2.5)

    def test_single_number(self):
        self.assertAlmostEqual(multiply_num([5]), 5)

    def test_zero_number(self):
        self.assertEqual(multiply_num([]), ZeroDivisionError)

    def test_negative_numbers(self):
        self.assertAlmostEqual(multiply_num([-1, -2, -3, -4]), -2.5)

    def test_large_numbers(self):
        self.assertAlmostEqual(multiply_num([10000, 20000, 30000]), 20000)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(multiply_num([1.5, 2.5, 3.5]), 2.5)

    def test_string_input(self):
        self.assertRaises(TypeError, multiply_num, ['1', '2', '3'])

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, multiply_num, [1, 'two', 3])
