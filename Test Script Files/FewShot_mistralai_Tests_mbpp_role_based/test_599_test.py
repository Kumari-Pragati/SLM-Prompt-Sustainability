import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_positive_integer(self):
        result = sum_average(5)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], 15)
        self.assertAlmostEqual(result[1], 3.0)

    def test_zero(self):
        result = sum_average(0)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 0)
        self.assertAlmostEqual(result[1], 0.0)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            sum_average(-1)
