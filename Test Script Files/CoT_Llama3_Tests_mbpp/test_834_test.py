import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_generate_matrix_valid_input(self):
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_generate_matrix_zero_input(self):
        self.assertEqual(generate_matrix(0), [])

    def test_generate_matrix_negative_input(self):
        with self.assertRaises(TypeError):
            generate_matrix(-1)

    def test_generate_matrix_one_input(self):
        self.assertEqual(generate_matrix(1), [[1]])

    def test_generate_matrix_large_input(self):
        self.assertEqual(generate_matrix(5), [[1, 2, 3, 4, 5], [16, 15, 14, 13, 6], [11, 12, 9, 8, 7], [10, 5, 6, 7, 3], [4, 3, 2, 1, 9]])
