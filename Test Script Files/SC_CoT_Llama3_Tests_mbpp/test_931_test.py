import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 6)
        self.assertEqual(sum_series(3), 14)

    def test_edge_cases(self):
        self.assertEqual(sum_series(-1), 0)
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(10), 385)

    def test_special_cases(self):
        self.assertEqual(sum_series(5), 55)
        self.assertEqual(sum_series(10), 385)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_series('a')
