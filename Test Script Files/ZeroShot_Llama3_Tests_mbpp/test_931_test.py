import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_sum_series(self):
        self.assertAlmostEqual(sum_series(1), 1)
        self.assertAlmostEqual(sum_series(2), 5/4)
        self.assertAlmostEqual(sum_series(3), 36/9)
        self.assertAlmostEqual(sum_series(4), 100/16)
        self.assertAlmostEqual(sum_series(5), 225/25)
        self.assertAlmostEqual(sum_series(6), 441/36)
        self.assertAlmostEqual(sum_series(7), 784/49)
        self.assertAlmostEqual(sum_series(8), 1331/64)
        self.assertAlmostEqual(sum_series(9), 1936/81)
        self.assertAlmostEqual(sum_series(10), 2520/100)

    def test_sum_series_edge_cases(self):
        self.assertAlmostEqual(sum_series(0), 0)
        self.assertAlmostEqual(sum_series(-1), 0)

    def test_sum_series_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_series('a')
        with self.assertRaises(TypeError):
            sum_series(None)
