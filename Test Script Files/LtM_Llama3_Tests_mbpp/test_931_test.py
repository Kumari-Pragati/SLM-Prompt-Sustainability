import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 6)
        self.assertEqual(sum_series(3), 14)

    def test_edge_cases(self):
        self.assertEqual(sum_series(-1), 0)
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(100), 5050)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_series('a')

    def test_complex_inputs(self):
        self.assertEqual(sum_series(5), 56)
        self.assertEqual(sum_series(10), 385)
