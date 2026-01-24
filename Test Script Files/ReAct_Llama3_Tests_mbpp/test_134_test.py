import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_even_sum(self):
        self.assertEqual(check_last([2, 4, 6], 3, 1), "EVEN")

    def test_odd_sum(self):
        self.assertEqual(check_last([1, 3, 5], 3, 1), "ODD")

    def test_zero_sum(self):
        self.assertEqual(check_last([0, 0, 0], 3, 1), "EVEN")

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            check_last([], 0, 1)

    def test_invalid_p(self):
        with self.assertRaises(TypeError):
            check_last([1, 2, 3], 3, 'a')

    def test_array_with_negative_numbers(self):
        self.assertEqual(check_last([-1, 2, 3], 3, 1), "EVEN")

    def test_array_with_zero_and_negative_numbers(self):
        self.assertEqual(check_last([0, -1, 2], 3, 1), "EVEN")

    def test_array_with_zero_and_positive_numbers(self):
        self.assertEqual(check_last([0, 1, 2], 3, 1), "EVEN")
