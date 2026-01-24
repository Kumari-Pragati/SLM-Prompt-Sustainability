import unittest
from mbpp_652_code import Iterable
from six.moves import zip
from six.moves import range

def matrix_to_list(test_list):
  temp = [ele for sub in test_list for ele in sub]
  res = list(zip(*temp))
  return (str(res))

class TestMatrixToList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(matrix_to_list([]), '[]')

    def test_single_element_list(self):
        self.assertEqual(matrix_to_list([[1]]), '[1]')

    def test_single_row_matrix(self):
        self.assertEqual(matrix_to_list([[1, 2, 3]]), '[1, 2, 3]')

    def test_single_column_matrix(self):
        self.assertEqual(matrix_to_list([[1], [2], [3]]), '[1, 2, 3]')

    def test_multi_row_multi_column_matrix(self):
        self.assertEqual(matrix_to_list([[1, 2], [3, 4]]), '[1, 3, 2, 4]')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            matrix_to_list(1)

        with self.assertRaises(TypeError):
            matrix_to_list('str')

        with self.assertRaises(TypeError):
            matrix_to_list([1, 2])
