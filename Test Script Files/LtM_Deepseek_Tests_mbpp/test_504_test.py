import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 9)
        self.assertEqual(sum_Of_Series(3), 36)

    def test_edge_conditions(self):
        self.assertEqual(sum_Of_Series(0), 0)
        self.assertEqual(sum_Of_Series(-1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Of_Series(10), 3025)
        self.assertEqual(sum_Of_Series(100), 3348276)

    def test_complex_cases(self):
        self.assertEqual(sum_Of_Series(1000), 250023163150)
