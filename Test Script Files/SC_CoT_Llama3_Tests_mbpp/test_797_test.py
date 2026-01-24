import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):

    def test_sum_in_range_positive(self):
        self.assertEqual(sum_in_Range(1, 5), 9)

    def test_sum_in_range_negative(self):
        self.assertEqual(sum_in_Range(-1, -5), 9)

    def test_sum_in_range_zero(self):
        self.assertEqual(sum_in_Range(0, 0), 0)

    def test_sum_in_range_single(self):
        self.assertEqual(sum_in_Range(1, 1), 0)

    def test_sum_in_range_empty(self):
        with self.assertRaises(TypeError):
            sum_in_Range(None, 5)

    def test_sum_in_range_invalid_type(self):
        with self.assertRaises(TypeError):
            sum_in_Range('a', 5)

    def test_sum_in_range_non_integer(self):
        with self.assertRaises(TypeError):
            sum_in_Range(1.5, 5)

    def test_sum_in_range_non_integer2(self):
        with self.assertRaises(TypeError):
            sum_in_Range(1, 5.5)
