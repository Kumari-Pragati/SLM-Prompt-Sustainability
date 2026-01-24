import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_multiply_single_number(self):
        self.assertEqual(multiply_num([1]), 1)

    def test_multiply_multiple_numbers(self):
        self.assertEqual(multiply_num([1, 2, 3, 4]), 2.5)

    def test_multiply_zero(self):
        self.assertEqual(multiply_num([0]), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply_num([-1, -2, -3, -4]), -2.5)

    def test_multiply_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])

    def test_multiply_single_zero(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([0])
