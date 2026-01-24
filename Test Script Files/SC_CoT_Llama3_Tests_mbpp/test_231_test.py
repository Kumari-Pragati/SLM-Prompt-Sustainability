import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_typical_input(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 3
        self.assertEqual(max_sum(tri, n), 9)

    def test_edge_case(self):
        tri = [[1, 2, 3], [4, 5, 6]]
        n = 2
        self.assertEqual(max_sum(tri, n), 6)

    def test_edge_case_2(self):
        tri = [[1, 2, 3]]
        n = 1
        self.assertEqual(max_sum(tri, n), 1)

    def test_edge_case_3(self):
        tri = [[1]]
        n = 1
        self.assertEqual(max_sum(tri, n), 1)

    def test_edge_case_4(self):
        tri = [[1, 2]]
        n = 2
        self.assertEqual(max_sum(tri, n), 2)

    def test_invalid_input(self):
        tri = [[1, 2, 3]]
        n = 0
        with self.assertRaises(IndexError):
            max_sum(tri, n)

    def test_invalid_input_2(self):
        tri = [[1, 2, 3]]
        n = -1
        with self.assertRaises(IndexError):
            max_sum(tri, n)
