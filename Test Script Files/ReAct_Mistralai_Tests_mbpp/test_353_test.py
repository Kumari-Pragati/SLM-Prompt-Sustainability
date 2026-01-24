import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(TypeError, remove_column, [], 0)

    def test_single_element_list(self):
        self.assertEqual(remove_column([1, 2, 3], 0), [2, 3])
        self.assertEqual(remove_column([[1], [2], [3]], 0), [[], [2], [3]])

    def test_list_with_one_column(self):
        self.assertEqual(remove_column([[1, 2], [3, 4], [5, 6]], 0), [[2], [4], [6]])
        self.assertEqual(remove_column([[1, 2], [3, 4], [5, 6]], 1), [[1], [3], [5]])

    def test_list_with_multiple_columns(self):
        self.assertEqual(remove_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
                         [[1, 3], [4, 6], [7, 9]])
        self.assertEqual(remove_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2),
                         [[1, 2], [4, 5], [7, 8]])

    def test_negative_index(self):
        self.assertRaises(IndexError, remove_column, [[1, 2], [3, 4]], -1)

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, remove_column, [[1, 2], [3, 4]], 2)

    def test_list_with_non_list_elements(self):
        self.assertRaises(TypeError, remove_column, [1, [2, 3], 4], 1)
