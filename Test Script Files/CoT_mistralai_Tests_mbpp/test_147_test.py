import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):

    def test_typical_case(self):
        tri = [[3, 8, 8, 5, 7],
               [2, 2, 9, 4, 7],
               [8, 7, 6, 4, 6],
               [8, 8, 4, 7, 7],
               [2, 2, 2, 3, 3]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 22)

    def test_edge_case_1(self):
        tri = [[1], [1]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 1)

    def test_edge_case_2(self):
        tri = [[1, 1], [1, 1]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 2)

    def test_edge_case_3(self):
        tri = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(max_path_sum(tri, len(tri), len(tri[0])), 3)

    def test_invalid_input_1(self):
        with self.assertRaises(ValueError):
            max_path_sum(None, 1, 1)

    def test_invalid_input_2(self):
        with self.assertRaises(ValueError):
            max_path_sum(tri, 0, len(tri[0]))

    def test_invalid_input_3(self):
        with self.assertRaises(ValueError):
            max_path_sum(tri, len(tri), 0)
