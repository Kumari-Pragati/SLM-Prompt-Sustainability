import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(series_sum(0), 0)
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 4)
        self.assertEqual(series_sum(3), 10)
        self.assertEqual(series_sum(4), 20)

    def test_edge_cases(self):
        self.assertEqual(series_sum(-1), 0)
        self.assertEqual(series_sum(0.5), 0.16666666666666666)
        self.assertEqual(series_sum(10.5), 385.8333333333333)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            series_sum('a')
        with self.assertRaises(TypeError):
            series_sum(None)
