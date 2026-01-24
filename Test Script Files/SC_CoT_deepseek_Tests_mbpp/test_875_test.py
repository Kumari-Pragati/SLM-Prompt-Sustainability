import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(min_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_edge_case(self):
        self.assertAlmostEqual(min_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(min_difference([(-1000, 1000), (0, 0), (1000, -1000)]), 2000)

    def test_special_case(self):
        self.assertAlmostEqual(min_difference([(10, 20), (20, 10), (30, 40)]), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_difference("not a list")
        with self.assertRaises(TypeError):
            min_difference([(1, "not a number"), (2, 3)])
