import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative(self):
        self.assertEqual(sum_series(-1), 0)

    def test_one(self):
        self.assertEqual(sum_series(1), 1)

    def test_two(self):
        self.assertEqual(sum_series(2), 3)

    def test_positive(self):
        self.assertEqual(sum_series(5), 15)

    def test_large(self):
        self.assertEqual(sum_series(10), 385)

    def test_edge_case(self):
        self.assertEqual(sum_series(1000), 3180505276075)
