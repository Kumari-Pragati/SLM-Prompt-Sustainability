import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_average(3), (6, 2.0))

    def test_edge_case_min(self):
        self.assertEqual(sum_average(1), (1, 1.0))

    def test_edge_case_max(self):
        self.assertEqual(sum_average(100), (5050, 50.5))

    def test_corner_case_zero(self):
        self.assertEqual(sum_average(0), (0, None))
