import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_difference(10), 2640)

    def test_small_number(self):
        self.assertEqual(sum_difference(1), 0)

    def test_large_number(self):
        self.assertEqual(sum_difference(100), 25164150)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            sum_difference(-10)

    def test_zero(self):
        self.assertEqual(sum_difference(0), 0)
