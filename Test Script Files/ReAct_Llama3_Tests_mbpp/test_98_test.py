import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(multiply_num([1]), 1)

    def test_multiple_numbers(self):
        self.assertEqual(multiply_num([1, 2, 3]), 2)

    def test_zero_in_list(self):
        self.assertEqual(multiply_num([1, 0, 3]), 1)

    def test_all_zeros(self):
        self.assertEqual(multiply_num([0, 0, 0]), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([0])

    def test_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])
