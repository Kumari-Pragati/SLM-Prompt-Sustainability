import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):

    def test_typical_case(self):
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_empty_matrix(self):
        M = []
        expected_output = []
        self.assertEqual(sort_matrix(M), expected_output)

    def test_single_row_matrix(self):
        M = [[1, 2, 3]]
        expected_output = [[3, 2, 1]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_single_column_matrix(self):
        M = [[1], [2], [3]]
        expected_output = [[3], [2], [1]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_duplicate_rows(self):
        M = [[1, 2, 3], [1, 2, 3]]
        expected_output = [[3, 2, 1], [3, 2, 1]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_negative_numbers(self):
        M = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        expected_output = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_large_numbers(self):
        M = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        expected_output = [[100, 200, 300], [400, 500, 600], [700, 800, 900]]
        self.assertEqual(sort_matrix(M), expected_output)
