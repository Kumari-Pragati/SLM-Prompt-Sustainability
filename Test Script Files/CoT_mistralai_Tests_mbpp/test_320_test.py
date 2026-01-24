import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(2), 3)
        self.assertEqual(sum_difference(3), 10)
        self.assertEqual(sum_difference(10), 285)
        self.assertEqual(sum_difference(100), 3178025)

    def test_zero(self):
        self.assertEqual(sum_difference(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_difference(-1), 4)
        self.assertEqual(sum_difference(-2), 25)
        self.assertEqual(sum_difference(-3), 100)
        self.assertEqual(sum_difference(-10), 285)
        self.assertEqual(sum_difference(-100), 3178025)

    def test_large_positive_numbers(self):
        self.assertAlmostEqual(sum_difference(1e6), 3.0e12)

    def test_invalid_input(self):
        self.assertRaises(TypeError, sum_difference, 'not a number')
        self.assertRaises(TypeError, sum_difference, -1.5e-308)
