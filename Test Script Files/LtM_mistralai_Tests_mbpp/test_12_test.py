import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):

    def test_simple_matrix(self):
        self.assertEqual(sort_matrix([[1, 2], [3, 4]]), [[[1, 2], [3, 4]], [[3, 4], [1, 2]]])
        self.assertEqual(sort_matrix([[5, 3], [2, 4]]), [[[2, 4], [5, 3]], [[5, 3], [2, 4]]])

    def test_edge_cases(self):
        self.assertEqual(sort_matrix([[1], [2]]), [[[1], [2]], [[2], [1]]])
        self.assertEqual(sort_matrix([[1], [2], [3]]), [[[1], [2], [3]], [[1, 2, 3], [1, 2, 3]]])
        self.assertEqual(sort_matrix([[1, 2], [2, 1]]), [[[1, 2], [2, 1]], [[1, 2], [2, 1]]])
        self.assertEqual(sort_matrix([[1, 2, 3], [1, 2, 3]]), [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]]])

    def test_complex_cases(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]])
        self.assertEqual(sort_matrix([[1000000000, 1], [1, 2]]), [[[1, 2], [1000000000, 1]], [[1, 2], [1000000000, 1]]])
