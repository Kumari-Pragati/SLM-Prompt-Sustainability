import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_multiply_num_single_value(self):
        self.assertEqual(multiply_num([1]), 1)

    def test_multiply_num_multiple_values(self):
        self.assertEqual(multiply_num([1, 2, 3]), 3)

    def test_multiply_num_zero(self):
        self.assertEqual(multiply_num([0, 1, 2]), 1)

    def test_multiply_num_negative(self):
        self.assertEqual(multiply_num([-1, 2, 3]), 3)

    def test_multiply_num_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])

    def test_multiply_num_single_zero(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([0])

    def test_multiply_num_multiple_zeros(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([0, 0, 0])
