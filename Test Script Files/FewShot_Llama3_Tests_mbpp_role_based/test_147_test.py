import unittest
from mbpp_147_code import max_path_sum

class TestMaxPathSum(unittest.TestCase):
    def test_typical_use_case(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)

    def test_edge_case_m_1_n_1(self):
        tri = [[1]]
        self.assertEqual(max_path_sum(tri, 1, 1), 1)

    def test_edge_case_m_2_n_2(self):
        tri = [[1, 2], [3, 4]]
        self.assertEqual(max_path_sum(tri, 2, 2), 4)

    def test_edge_case_m_3_n_3(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_path_sum(tri, 3, 3), 9)

    def test_invalid_input_m_0_n_0(self):
        tri = []
        with self.assertRaises(IndexError):
            max_path_sum(tri, 0, 0)

    def test_invalid_input_m_1_n_0(self):
        tri = [[1]]
        with self.assertRaises(IndexError):
            max_path_sum(tri, 1, 0)

    def test_invalid_input_m_0_n_1(self):
        tri = [[1, 2]]
        with self.assertRaises(IndexError):
            max_path_sum(tri, 0, 1)
