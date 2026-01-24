import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 5)
        self.assertEqual(max_difference([(10, 20), (30, 40), (50, 60)]), 50)

    def test_edge_conditions(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)
        self.assertEqual(max_difference([(1, 1000000), (2, 999999), (3, 1000001)]), 2)

    def test_boundary_conditions(self):
        self.assertEqual(max_difference([(0, 1000000000), (-1000000000, 0)]), 2000000000)
        self.assertEqual(max_difference([(-1, 1), (-2, 2), (-3, 3)]), 4)

    def test_complex_cases(self):
        self.assertEqual(max_difference([(1, 10), (20, 30), (40, 50)]), 30)
        self.assertEqual(max_difference([(100, 200), (300, 400), (500, 600)]), 500)
