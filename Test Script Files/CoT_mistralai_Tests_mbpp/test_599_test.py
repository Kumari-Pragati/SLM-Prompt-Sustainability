import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_sum_average_positive_integer(self):
        self.assertEqual(sum_average(3), (6, 2))
        self.assertEqual(sum_average(5), (15, 3))
        self.assertEqual(sum_average(10), (55, 5.5))

    def test_sum_average_zero(self):
        self.assertEqual(sum_average(0), (0, 0))

    def test_sum_average_negative_integer(self):
        self.assertRaises(ValueError, sum_average, -3)

    def test_sum_average_floating_point(self):
        self.assertAlmostEqual(sum_average(3.5), (11.75, 3.25))
