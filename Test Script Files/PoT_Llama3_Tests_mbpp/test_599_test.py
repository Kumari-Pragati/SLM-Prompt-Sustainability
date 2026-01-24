import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_average(5), (15, 3.0))

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sum_average(0)

    def test_edge_case_one(self):
        self.assertEqual(sum_average(1), (1, 1.0))

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            sum_average(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            sum_average(3.5)

    def test_edge_case_large(self):
        self.assertEqual(sum_average(1000), (500500, 500.5))

    def test_edge_case_small(self):
        self.assertEqual(sum_average(1), (1, 1.0))
