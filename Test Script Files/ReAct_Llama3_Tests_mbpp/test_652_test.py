import unittest
from mbpp_652_code import matrix_to_list

class TestMatrixToList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [4, 5, 6]]), '[(1, 2, 3), (4, 5, 6)]')

    def test_empty_list(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(matrix_to_list([[1]]), '[(1,)]')

    def test_single_element_sublist(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], [1]]), '[(1, 2, 3), (1)]')

    def test_matrix_with_duplicates(self):
        self.assertEqual(matrix_to_list([[1, 2, 2], [3, 4, 4]]), '[(1, 2, 2), (3, 4, 4)]')

    def test_matrix_with_empty_sublist(self):
        self.assertEqual(matrix_to_list([[1, 2, 3], []]), '[(1, 2, 3), ()]')

    def test_matrix_with_empty_sublist_and_duplicates(self):
        self.assertEqual(matrix_to_list([[1, 2, 2], [], [3, 4, 4]]), '[(1, 2, 2), (), (3, 4, 4)]')
