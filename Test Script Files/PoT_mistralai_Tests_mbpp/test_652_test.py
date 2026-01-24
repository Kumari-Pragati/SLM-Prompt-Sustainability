import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(matrix_to_list([[1, 2], [3, 4]]), ['12', '34'])
        self.assertEqual(matrix_to_list([['a', 'b'], ['c', 'd']]), ['ab', 'cd'])

    def test_edge_case_empty_list(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_edge_case_single_row_or_column(self):
        self.assertEqual(matrix_to_list([[1]]), ['1'])
        self.assertEqual(matrix_to_list([[1, 2], ]), ['12'])
        self.assertEqual(matrix_to_list([[1, 2], [3]]), ['12', '3'])
        self.assertEqual(matrix_to_list([[1, 2], ]), ['12'])

    def test_corner_case_mixed_types(self):
        self.assertEqual(matrix_to_list([[1, 2], [3, 'a']]), ['12', '3a'])
