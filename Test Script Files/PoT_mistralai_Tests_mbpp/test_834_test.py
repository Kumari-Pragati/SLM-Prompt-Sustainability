import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(generate_matrix(0), [])

    def test_single_element(self):
        self.assertEqual(generate_matrix(1), [[0]])

    def test_small_matrix(self):
        self.assertEqual(generate_matrix(2), [[0, 1], [2, 0]])

    def test_large_matrix(self):
        self.assertEqual(generate_matrix(5), [[0, 1, 2, 3, 4],
                                                [5, 0, 6, 7, 8],
                                                [9, 10, 0, 11, 12],
                                                [13, 14, 15, 0, 16],
                                                [17, 18, 19, 20, 0]])

    def test_negative_input(self):
        self.assertRaises(ValueError, generate_matrix, -1)
