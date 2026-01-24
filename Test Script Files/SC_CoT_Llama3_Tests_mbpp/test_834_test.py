import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_generate_matrix_typical(self):
        self.assertEqual(generate_matrix(3),
                         [[1, 2, 3],
                          [8, 9, 4],
                          [7, 6, 5]])

    def test_generate_matrix_edge_case(self):
        self.assertEqual(generate_matrix(1),
                         [[1]])

    def test_generate_matrix_edge_case2(self):
        self.assertEqual(generate_matrix(0),
                         [])

    def test_generate_matrix_edge_case3(self):
        self.assertEqual(generate_matrix(2),
                         [[1, 2],
                          [4, 3]])

    def test_generate_matrix_edge_case4(self):
        self.assertEqual(generate_matrix(4),
                         [[1, 2, 3, 4],
                          [13, 14, 15, 6],
                          [12, 11, 10, 5],
                          [9, 8, 7, 16]])

    def test_generate_matrix_invalid_input(self):
        with self.assertRaises(TypeError):
            generate_matrix('a')
