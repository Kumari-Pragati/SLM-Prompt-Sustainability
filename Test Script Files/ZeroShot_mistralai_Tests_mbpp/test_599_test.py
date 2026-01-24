import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_sum_average_positive_numbers(self):
        self.assertAlmostEqual(sum_average(3), (6.0, 2.0))
        self.assertAlmostEqual(sum_average(5), (15.0, 3.0))
        self.assertAlmostEqual(sum_average(10), (55.0, 5.5))

    def test_sum_average_zero(self):
        self.assertEqual(sum_average(0), (0.0, None))

    def test_sum_average_negative_numbers(self):
        self.assertRaises(ValueError, sum_average, -1)
        self.assertRaises(ValueError, sum_average, -2)
        self.assertRaises(ValueError, sum_average, -3)
