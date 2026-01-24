import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 2)
        self.assertEqual(sum_series(3), 9)

    def test_edge_and_boundary(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1000), 333333336)
        self.assertAlmostEqual(sum_series(math.sqrt(2)), math.sqrt(2))
