import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):
    def test_sort_matrix_typical(self):
        self.assertEqual(sort_matrix([[1, 2], [3, 0]]), [[[0, 3], [2, 1]]])
        self.assertEqual(sort_matrix([[5, 1, 9], [2, 6, 3], [4, 8, 7]]), [[[2, 3, 6], [4, 8, 7], [5, 1, 9]]])

    def test_sort_matrix_edge(self):
        self.assertEqual(sort_matrix([[0], [1], [2]]), [[[0], [1], [2]]])
        self.assertEqual(sort_matrix([[1], [2], [3]]), [[[1], [2], [3]]])
        self.assertEqual(sort_matrix([[1, 1], [2, 2], [3, 3]]), [[[1, 1], [2, 2], [3, 3]]])

    def test_sort_matrix_corner(self):
        self.assertEqual(sort_matrix([[1000000000], [1, 2]]), [[[1, 2], [1000000000]]])
        self.assertEqual(sort_matrix([[1, 2], [1000000000]]), [[[1, 2], [1000000000]]])
        self.assertEqual(sort_matrix([[1, 2], [1, 2]]), [[[1, 1], [2, 2]]])
