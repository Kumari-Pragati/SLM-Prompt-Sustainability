import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_typical_use_case(self):
        M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_output = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_edge_condition(self):
        M = [[1]]
        expected_output = [[1]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_boundary_condition(self):
        M = [[0, 0], [0, 0]]
        expected_output = [[0, 0], [0, 0]]
        self.assertEqual(sort_matrix(M), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_matrix('not a matrix')
