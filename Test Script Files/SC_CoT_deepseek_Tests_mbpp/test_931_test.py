import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(sum_series(5), 122.5)

    def test_boundary_case(self):
        self.assertAlmostEqual(sum_series(0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(sum_series(1), 1)

    def test_large_number_case(self):
        self.assertAlmostEqual(sum_series(100), 338350.0)

    def test_negative_number_case(self):
        with self.assertRaises(ValueError):
            sum_series(-5)
