import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):

    def test_sort_matrix(self):
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_sort_matrix_with_negative_numbers(self):
        M = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        expected_output = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_sort_matrix_with_zeroes(self):
        M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected_output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_sort_matrix_with_empty_matrix(self):
        M = []
        expected_output = []
        self.assertEqual(sort_matrix(M), expected_output)
