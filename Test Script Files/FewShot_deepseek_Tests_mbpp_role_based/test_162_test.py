import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_series(5), 14)

    def test_boundary_condition(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 4)

    def test_edge_condition(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(-1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_series('5')
