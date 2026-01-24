import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(series_sum(3), 14.0/6.0)

    def test_zero_case(self):
        self.assertEqual(series_sum(0), 0)

    def test_negative_case(self):
        self.assertEqual(series_sum(-1), 0)

    def test_large_number_case(self):
        self.assertAlmostEqual(series_sum(10), 140.0/6.0)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            series_sum("invalid")

    def test_invalid_input_float(self):
        with self.assertRaises(TypeError):
            series_sum(3.5)
