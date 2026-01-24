import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(series_sum(1), 1.0/1.0)
        self.assertAlmostEqual(series_sum(2), (1.0/1.0 + 2.0/2.0))
        self.assertAlmostEqual(series_sum(3), (1.0/1.0 + 2.0/2.0 + 3.0/3.0))

    def test_edge_cases(self):
        self.assertAlmostEqual(series_sum(0), 0.0)
        self.assertAlmostEqual(series_sum(10), sum([i/(i+1) for i in range(1, 11)]))

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            series_sum('a')
        with self.assertRaises(ValueError):
            series_sum(-1)
