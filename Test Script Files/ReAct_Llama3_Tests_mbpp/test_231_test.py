import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_single_element(self):
        tri = [[1]]
        self.assertEqual(max_sum(tri, 1), 1)

    def test_two_elements(self):
        tri = [[1], [2]]
        self.assertEqual(max_sum(tri, 2), 2)

    def test_three_elements(self):
        tri = [[1], [2, 3], [4, 5, 6]]
        self.assertEqual(max_sum(tri, 3), 6)

    def test_four_elements(self):
        tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        self.assertEqual(max_sum(tri, 4), 10)

    def test_edge_case(self):
        tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
        self.assertEqual(max_sum(tri, 5), 15)

    def test_error_case(self):
        tri = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
        with self.assertRaises(IndexError):
            max_sum(tri, 0)
