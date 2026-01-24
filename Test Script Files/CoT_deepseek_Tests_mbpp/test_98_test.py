import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4]), 2.4)

    def test_single_number(self):
        self.assertEqual(multiply_num([5]), 5)

    def test_zero_number(self):
        self.assertEqual(multiply_num([]), 0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(multiply_num([-1, -2, -3]), -2.0)

    def test_zero_in_list(self):
        self.assertEqual(multiply_num([0, 2, 3]), 0)

    def test_large_numbers(self):
        self.assertAlmostEqual(multiply_num([10**6, 2*10**6, 3*10**6]), 2*10**6)

    def test_float_numbers(self):
        self.assertAlmostEqual(multiply_num([1.5, 2.5, 3.5]), 2.5)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            multiply_num(['1', '2', '3'])

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            multiply_num(123)
