import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(generate_matrix(0), [])

    def test_single_element(self):
        self.assertEqual(generate_matrix(1), [[1]])

    def test_square_matrix(self):
        self.assertEqual(generate_matrix(2), [[1, 2], [3, 4]])

    def test_larger_square_matrix(self):
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_non_square_matrix(self):
        self.assertEqual(generate_matrix(4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    def test_edge_case(self):
        self.assertEqual(generate_matrix(1), [[1]])

    def test_edge_case2(self):
        self.assertEqual(generate_matrix(2), [[1, 2], [3, 4]])

    def test_edge_case3(self):
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_edge_case4(self):
        self.assertEqual(generate_matrix(4), [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
