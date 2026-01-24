import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):
    def test_small_positive_integer(self):
        self.assertEqual(sum_Of_Series(3), 36)

    def test_large_positive_integer(self):
        self.assertEqual(sum_Of_Series(10), 4050)

    def test_zero(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            sum_Of_Series(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            sum_Of_Series(3.5)
