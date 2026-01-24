import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(generate_matrix(3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertListEqual(generate_matrix(5), [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(generate_matrix(0), [])
        self.assertListEqual(generate_matrix(1), [[1]])
        self.assertListEqual(generate_matrix(-1), [])

    def test_special_cases(self):
        self.assertListEqual(generate_matrix(2), [[1, 2], [3, 4]])
        self.assertListEqual(generate_matrix(4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
