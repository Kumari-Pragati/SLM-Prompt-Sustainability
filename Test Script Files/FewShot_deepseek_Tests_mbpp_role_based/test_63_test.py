import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 5)

    def test_edge_case(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_boundary_case(self):
        self.assertEqual(max_difference([(0, 1000000), (1, 2), (3, 4)]), 999999)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_difference("not a list")

        with self.assertRaises(ValueError):
            max_difference([(1, "not a number"), (2, 3), (4, 5)])
