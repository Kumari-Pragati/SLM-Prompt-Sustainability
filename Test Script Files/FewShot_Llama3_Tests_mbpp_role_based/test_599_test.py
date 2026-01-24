import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_sum_average_positive_number(self):
        result = sum_average(5)
        self.assertEqual(result[0], 15)
        self.assertAlmostEqual(result[1], 3.0)

    def test_sum_average_zero(self):
        result = sum_average(0)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 0)

    def test_sum_average_negative_number(self):
        result = sum_average(-5)
        self.assertEqual(result[0], -10)
        self.assertAlmostEqual(result[1], -2.0)

    def test_sum_average_non_integer(self):
        with self.assertRaises(TypeError):
            sum_average(3.5)
