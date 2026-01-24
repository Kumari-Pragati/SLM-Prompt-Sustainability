import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 3)
        self.assertEqual(series_sum(3), 6)
        self.assertEqual(series_sum(4), 10)

    def test_edge_cases(self):
        self.assertEqual(series_sum(0), 0)
        self.assertEqual(series_sum(-1), 0)
        self.assertEqual(series_sum(5), 15)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            series_sum('a')

    def test_boundary_cases(self):
        self.assertEqual(series_sum(-2), 0)
        self.assertEqual(series_sum(-3), 0)
        self.assertEqual(series_sum(10), 55)
