import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_generate_matrix_with_positive_n(self):
        self.assertEqual(generate_matrix(1), [[1]])
        self.assertEqual(generate_matrix(2), [[1, 2], [4, 3]])
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_generate_matrix_with_zero_n(self):
        self.assertEqual(generate_matrix(0), [])

    def test_generate_matrix_with_negative_n(self):
        self.assertEqual(generate_matrix(-1), [])
