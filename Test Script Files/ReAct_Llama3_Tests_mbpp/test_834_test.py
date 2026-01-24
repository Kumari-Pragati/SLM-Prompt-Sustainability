import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(generate_matrix(0), [])

    def test_single_element_matrix(self):
        self.assertEqual(generate_matrix(1), [[1]])

    def test_small_matrix(self):
        self.assertEqual(generate_matrix(2), [[1, 2], [3, 4]])

    def test_large_matrix(self):
        self.assertEqual(generate_matrix(5), [[1, 2, 3, 4, 5],
                                              [6, 7, 8, 9, 10],
                                              [11, 12, 13, 14, 15],
                                              [16, 17, 18, 19, 20],
                                              [21, 22, 23, 24, 25]])

    def test_matrix_with_duplicates(self):
        self.assertEqual(generate_matrix(3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_matrix_with_zero(self):
        self.assertEqual(generate_matrix(0), [])
