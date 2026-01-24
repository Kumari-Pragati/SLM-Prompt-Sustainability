import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual(generate_matrix(0), [])

    def test_single_element_matrix(self):
        self.assertEqual(generate_matrix(1), [[1]])

    def test_2x2_matrix(self):
        self.assertEqual(generate_matrix(2), [[1, 2], [4, 3]])

    def test_3x3_matrix(self):
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_4x4_matrix(self):
        self.assertEqual(generate_matrix(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])

    def test_negative_size(self):
        self.assertEqual(generate_matrix(-1), [])

    def test_large_size(self):
        large_matrix = generate_matrix(10)
        self.assertEqual(len(large_matrix), 10)
        self.assertEqual(len(large_matrix[0]), 10)
        self.assertEqual(large_matrix[0][0], 1)
        self.assertEqual(large_matrix[9][9], 100)
