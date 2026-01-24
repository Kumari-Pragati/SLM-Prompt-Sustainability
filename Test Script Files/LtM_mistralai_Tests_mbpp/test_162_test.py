import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 3)
        self.assertEqual(sum_series(3), 5)
        self.assertEqual(sum_series(4), 7)

    def test_edge_input(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(5), 15)
        self.assertEqual(sum_series(6), 17)
