import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_empty_input(self):
        self.assertListEqual(generate_matrix(0), [])

    def test_simple_input(self):
        self.assertListEqual(generate_matrix(1), [[0]])
        self.assertListEqual(generate_matrix(2), [[0, 1], [0, 0]])
        self.assertListEqual(generate_matrix(3), [[0, 1, 2], [0, 2, 3], [1, 2, 3]])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(generate_matrix(-1), [])
        self.assertListEqual(generate_matrix(1000), [[0, 1, 2, ..., 998, 999]])

    def test_complex_input(self):
        self.assertListEqual(generate_matrix(4), [[0, 1, 2, 3], [1, 5, 6, 7], [2, 6, 13, 14], [3, 7, 14, 20]])
        self.assertListEqual(generate_matrix(5), [[0, 1, 2, 3, 4], [1, 6, 7, 8, 9], [2, 7, 13, 14, 15], [3, 8, 14, 20, 21], [4, 9, 15, 21, 26]])
