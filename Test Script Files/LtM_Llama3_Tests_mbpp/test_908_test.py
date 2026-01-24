import unittest
from mbpp_908_code import find_fixed_point

class TestFindFixedPoint(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(find_fixed_point([0, 1, 2, 3, 4, 5], 6), 0)

    def test_edge_case_empty_input(self):
        with self.assertRaises(IndexError):
            find_fixed_point([], 0)

    def test_edge_case_single_element_input(self):
        self.assertEqual(find_fixed_point([0], 1), 0)

    def test_edge_case_zero_input(self):
        self.assertEqual(find_fixed_point([0], 1), 0)

    def test_edge_case_negative_input(self):
        self.assertEqual(find_fixed_point([-1, 0, 1], 3), 0)

    def test_edge_case_max_input(self):
        self.assertEqual(find_fixed_point([5, 4, 3, 2, 1, 0], 6), 5)

    def test_edge_case_min_input(self):
        self.assertEqual(find_fixed_point([-5, -4, -3, -2, -1, 0], 6), 0)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            find_fixed_point("hello", 0)
