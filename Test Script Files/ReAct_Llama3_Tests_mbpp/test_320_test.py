import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_small_positive(self):
        self.assertEqual(sum_difference(3), 0)

    def test_large_positive(self):
        self.assertEqual(sum_difference(100), 25164150)

    def test_zero(self):
        self.assertEqual(sum_difference(0), 0)

    def test_negative(self):
        with self.assertRaises(TypeError):
            sum_difference(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            sum_difference(3.5)
