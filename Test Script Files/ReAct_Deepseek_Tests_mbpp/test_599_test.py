import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_average(5), (15, 3))

    def test_boundary_case_small_number(self):
        self.assertEqual(sum_average(1), (1, 1))

    def test_boundary_case_large_number(self):
        self.assertEqual(sum_average(1000), (500500, 5005))

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sum_average(0)
