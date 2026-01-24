import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative_input(self):
        self.assertEqual(sum_series(-1), 0)

    def test_positive_input(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 3)
        self.assertEqual(sum_series(3), 6)
        self.assertEqual(sum_series(4), 10)
        self.assertEqual(sum_series(5), 15)

    def test_edge_cases(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 3)
        self.assertEqual(sum_series(3), 6)
        self.assertEqual(sum_series(4), 10)
        self.assertEqual(sum_series(5), 15)

    def test_large_input(self):
        self.assertEqual(sum_series(10), 55)
        self.assertEqual(sum_series(20), 210)
        self.assertEqual(sum_series(30), 465)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            sum_series("a")
