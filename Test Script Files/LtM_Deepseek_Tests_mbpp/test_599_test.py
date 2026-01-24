import unittest
from mbpp_599_code import sum_average

class TestSumAverage(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_average(5), (15, 3))

    def test_boundary_conditions(self):
        self.assertEqual(sum_average(1), (1, 1))
        self.assertEqual(sum_average(0), (0, 0))

    def test_edge_cases(self):
        self.assertEqual(sum_average(-1), (0, 0))
        self.assertEqual(sum_average(1000), (500500, 500.5))

    def test_complex_cases(self):
        self.assertEqual(sum_average(10), (55, 5.5))
        self.assertEqual(sum_average(20), (210, 10.5))
