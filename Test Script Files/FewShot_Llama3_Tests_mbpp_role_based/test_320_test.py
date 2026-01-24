import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):
    def test_small_positive_integer(self):
        self.assertEqual(sum_difference(2), 0)

    def test_large_positive_integer(self):
        self.assertEqual(sum_difference(100), 25164150280)

    def test_zero(self):
        self.assertEqual(sum_difference(0), 0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            sum_difference(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            sum_difference('a')
