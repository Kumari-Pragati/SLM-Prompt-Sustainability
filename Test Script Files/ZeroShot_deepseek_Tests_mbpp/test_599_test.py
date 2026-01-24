import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_sum_average_positive_number(self):
        total, average = sum_average(5)
        self.assertEqual(total, 15)
        self.assertEqual(average, 3)

    def test_sum_average_zero(self):
        total, average = sum_average(0)
        self.assertEqual(total, 0)
        self.assertEqual(average, 0)

    def test_sum_average_negative_number(self):
        with self.assertRaises(ValueError):
            sum_average(-5)
