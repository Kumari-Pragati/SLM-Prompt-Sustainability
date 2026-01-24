import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):
    def test_simple_valid_input(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)

    def test_edge_case_empty_input(self):
        tri = []
        with self.assertRaises(IndexError):
            max_path_sum(tri, 0, 0)

    def test_edge_case_single_element_input(self):
        tri = [[1]]
        self.assertEqual(max_path_sum(tri, 1, 1), 1)

    def test_edge_case_two_elements_input(self):
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_path_sum(tri, 2, 2), 4)

    def test_edge_case_three_elements_input(self):
        tri = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_path_sum(tri, 2, 3), 6)

    def test_edge_case_max_path_sum_at_edge(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)

    def test_edge_case_max_path_sum_at_corner(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)

    def test_edge_case_max_path_sum_at_center(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)
