import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_edge_case(self):
        self.assertEqual(min_difference([(1, 1)]), 0)

    def test_boundary_case(self):
        self.assertEqual(min_difference([(0, 1000000)]), 1000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_difference("invalid input")
