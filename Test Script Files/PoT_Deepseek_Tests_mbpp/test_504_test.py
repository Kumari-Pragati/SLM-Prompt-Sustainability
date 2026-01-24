import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 9)
        self.assertEqual(sum_Of_Series(3), 36)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(10), 3025)

    def test_corner_cases(self):
        self.assertEqual(sum_Of_Series(-1), 0)
        self.assertEqual(sum_Of_Series(100), 3348276)
