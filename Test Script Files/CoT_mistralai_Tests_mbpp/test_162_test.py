import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_one(self):
        self.assertEqual(sum_series(1), 1)

    def test_positive_numbers(self):
        for n in range(2, 10):
            self.assertEqual(sum_series(n), n + sum_series(n - 2))

    def test_large_number(self):
        self.assertEqual(sum_series(100), 100 + sum_series(98))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_series(-1)

    def test_floats(self):
        with self.assertRaises(TypeError):
            sum_series(3.14)

    def test_strings(self):
        with self.assertRaises(TypeError):
            sum_series('abc')
