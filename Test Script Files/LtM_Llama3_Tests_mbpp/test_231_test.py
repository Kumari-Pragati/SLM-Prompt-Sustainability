import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_empty_input(self):
        tri = []
        self.assertEqual(max_sum(tri, 0), 0)

    def test_single_element_input(self):
        tri = [[1]]
        self.assertEqual(max_sum(tri, 1), 1)

    def test_two_element_input(self):
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_sum(tri, 2), 6)

    def test_three_element_input(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum(tri, 3), 18)

    def test_edge_case_input(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(max_sum(tri, 4), 18)

    def test_max_sum_at_edge(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        tri[3][1] = 100
        self.assertEqual(max_sum(tri, 4), 100)

    def test_max_sum_at_center(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        tri[2][2] = 100
        self.assertEqual(max_sum(tri, 4), 100)

    def test_max_sum_at_start(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        tri[1][0] = 100
        self.assertEqual(max_sum(tri, 4), 100)

    def test_max_sum_at_end(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        tri[3][2] = 100
        self.assertEqual(max_sum(tri, 4), 100)
