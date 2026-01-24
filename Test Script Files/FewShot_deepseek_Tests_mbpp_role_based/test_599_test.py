import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_average(5), (15, 3))

    def test_boundary_condition(self):
        self.assertEqual(sum_average(1), (1, 1))

    def test_edge_case(self):
        self.assertEqual(sum_average(0), (0, 0))

    def test_large_number(self):
        self.assertEqual(sum_average(1000), (500500, 5005))

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_average(-5)
