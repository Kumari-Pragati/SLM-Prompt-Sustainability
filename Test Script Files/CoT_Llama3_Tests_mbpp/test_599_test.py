import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_sum_average_positive(self):
        self.assertEqual(sum_average(5), (15, 3.0))

    def test_sum_average_zero(self):
        self.assertEqual(sum_average(0), (0, 0.0))

    def test_sum_average_negative(self):
        with self.assertRaises(ValueError):
            sum_average(-1)

    def test_sum_average_non_integer(self):
        with self.assertRaises(TypeError):
            sum_average(3.5)

    def test_sum_average_edge_case(self):
        self.assertEqual(sum_average(1), (1, 1.0))
