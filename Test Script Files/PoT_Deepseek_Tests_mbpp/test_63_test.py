import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 5)

    def test_edge_case_single_pair(self):
        self.assertEqual(max_difference([(1, 2)]), 1)

    def test_boundary_case_same_elements(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_difference([(-1, -2), (-3, -4), (-5, -6)]), 5)

    def test_zero_difference(self):
        self.assertEqual(max_difference([(0, 0), (0, 0), (0, 0)]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_difference("not a list")

        with self.assertRaises(TypeError):
            max_difference([(1, "not a number"), (2, 2), (3, 3)])

        with self.assertRaises(TypeError):
            max_difference([(1, 2), ("not a number", 2), (3, 3)])
