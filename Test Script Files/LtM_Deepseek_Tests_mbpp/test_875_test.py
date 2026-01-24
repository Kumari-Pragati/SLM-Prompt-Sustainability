import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_difference([(1, 2), (3, 4)]), 1)
        self.assertEqual(min_difference([(5, 10), (15, 20)]), 5)

    def test_edge_conditions(self):
        self.assertEqual(min_difference([(0, 0), (0, 0)]), 0)
        self.assertEqual(min_difference([(1, 1), (1, 1)]), 0)
        self.assertEqual(min_difference([(1, 2), (2, 1)]), 1)

    def test_boundary_conditions(self):
        self.assertEqual(min_difference([(0, 1000000), (1000000, 0)]), 1000000)
        self.assertEqual(min_difference([(float('-inf'), float('inf')), (float('inf'), float('-inf'))]), float('inf'))

    def test_complex_cases(self):
        self.assertEqual(min_difference([(1, 2), (3, 4), (5, 6)]), 1)
        self.assertEqual(min_difference([(10, 20), (30, 40), (50, 60)]), 10)
