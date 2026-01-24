import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(sum_series(1), 1.0)
        self.assertAlmostEqual(sum_series(2), 10.0)
        self.assertAlmostEqual(sum_series(3), 35.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(sum_series(0), 0.0)
        self.assertAlmostEqual(sum_series(1), 1.0)

    def test_boundary_cases(self):
        self.assertAlmostEqual(sum_series(10), 3850.0)
        self.assertAlmostEqual(sum_series(100), 3383500.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_series('a')
        with self.assertRaises(TypeError):
            sum_series(None)
