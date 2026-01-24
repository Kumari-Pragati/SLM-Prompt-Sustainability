import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_positive_number(self):
        self.assertAlmostEqual(series_sum(5), 15.0)

    def test_zero(self):
        self.assertAlmostEqual(series_sum(0), 0.0)

    def test_negative_number(self):
        self.assertAlmostEqual(series_sum(-5), -10.0)

    def test_non_integer(self):
        self.assertAlmostEqual(series_sum(3.5), 7.5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            series_sum("five")
