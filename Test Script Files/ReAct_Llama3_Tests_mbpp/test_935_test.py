import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(series_sum(0), 0)

    def test_positive(self):
        self.assertAlmostEqual(series_sum(5), 35.0)

    def test_negative(self):
        self.assertAlmostEqual(series_sum(-5), -35.0)

    def test_edge_case(self):
        self.assertAlmostEqual(series_sum(0.5), 0.5)

    def test_non_integer(self):
        self.assertAlmostEqual(series_sum(2.5), 5.0)

    def test_large_number(self):
        self.assertAlmostEqual(series_sum(100), 5050.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            series_sum('a')
