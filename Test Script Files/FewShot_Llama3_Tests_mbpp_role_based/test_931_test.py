import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(sum_series(5), 36)

    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative_number(self):
        self.assertEqual(sum_series(-5), 36)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            sum_series(5.5)

    def test_large_number(self):
        self.assertEqual(sum_series(100), 5050)

    def test_edge_case(self):
        self.assertEqual(sum_series(1), 1)
