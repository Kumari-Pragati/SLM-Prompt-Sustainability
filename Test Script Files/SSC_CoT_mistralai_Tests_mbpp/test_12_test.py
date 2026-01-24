import unittest
from mbpp_12_code import sort_matrix

class TestSortMatrix(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sort_matrix([[3, 5, 1], [7, 8, 6], [2, 9, 4]]), [[2, 9, 4], [3, 5, 1], [7, 8, 6]])
        self.assertEqual(sort_matrix([[1], [0], [5], [-1], [2]]) , [[-1], [0], [1], [2], [5]])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sort_matrix([[0], [0], [0]]) , [[0], [0], [0]])
        self.assertEqual(sort_matrix([[1000000000], [1000000000], [1000000000]]) , [[1000000000], [1000000000], [1000000000]])
        self.assertEqual(sort_matrix([[-1000000000], [-1000000000], [-1000000000]]) , [[-1000000000], [-1000000000], [-1000000000]])
        self.assertEqual(sort_matrix([[float('inf')], [float('inf')], [float('inf')]]) , [[float('inf'), float('inf'), float('inf')]])
        self.assertEqual(sort_matrix([[-float('inf')], [-float('inf')], [-float('inf')]]) , [[-float('inf'), -float('inf'), -float('inf')]])

    def test_special_or_corner_cases(self):
        self.assertEqual(sort_matrix([[1, 1], [1, 1]]) , [[[1, 1], [1, 1]]])
        self.assertEqual(sort_matrix([[1, 1, 1], [1, 1, 1]]) , [[[1, 1, 1], [1, 1, 1]]])
        self.assertEqual(sort_matrix([[1, 1], [2, 2]]) , [[[1, 1], [2, 2]]])
        self.assertEqual(sort_matrix([[1, 2], [2, 1]]) , [[[1, 2], [2, 1]]])
        self.assertEqual(sort_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) , [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sort_matrix(123)
        with self.assertRaises(TypeError):
            sort_matrix('abc')
        with self.assertRaises(TypeError):
            sort_matrix([1, 2, 3, 4, 5], 'sum')
