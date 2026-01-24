import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum(tri, 3), 9)

    def test_edge_case(self):
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_sum(tri, 2), 4)

    def test_edge_case2(self):
        tri = [[1, 2, 3], [4, 5]]
        self.assertEqual(max_sum(tri, 2), 5)

    def test_edge_case3(self):
        tri = [[1, 2, 3, 4], [5, 6, 7, 8]]
        self.assertEqual(max_sum(tri, 4), 9)

    def test_invalid_input(self):
        tri = [[1, 2, 3], [4, 5, 6]]
        with self.assertRaises(IndexError):
            max_sum(tri, 1)

    def test_invalid_input2(self):
        tri = [[1, 2, 3]]
        with self.assertRaises(IndexError):
            max_sum(tri, 0)
