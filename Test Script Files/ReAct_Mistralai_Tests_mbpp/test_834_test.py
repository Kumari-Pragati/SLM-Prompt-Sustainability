import unittest
from mbpp_834_code import generate_matrix

class TestGenerateMatrix(unittest.TestCase):

    def test_empty_matrix(self):
        self.assertEqual(generate_matrix(0), [])

    def test_single_row_matrix(self):
        result = generate_matrix(1)
        self.assertEqual(result, [[0]])

    def test_single_column_matrix(self):
        result = generate_matrix(1)
        self.assertEqual(result[0], [0])

    def test_square_matrix(self):
        result = generate_matrix(2)
        expected = [[0, 1], [2, 3]]
        self.assertEqual(result, expected)

    def test_large_matrix(self):
        result = generate_matrix(5)
        expected = [[0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9],
                    [10, 11, 12, 13, 14],
                    [15, 16, 17, 18, 19],
                    [20, 21, 22, 23, 24]]
        self.assertEqual(result, expected)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            generate_matrix(-1)
