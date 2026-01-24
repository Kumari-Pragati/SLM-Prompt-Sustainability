import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):
    def test_remove_column_from_list(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = remove_column(list1, 1)
        self.assertEqual(result, [[1, 3], [4, 6], [7, 9]])

    def test_remove_column_from_empty_list(self):
        list1 = []
        result = remove_column(list1, 0)
        self.assertEqual(result, [])

    def test_remove_column_from_list_with_single_element(self):
        list1 = [[1, 2, 3]]
        result = remove_column(list1, 1)
        self.assertEqual(result, [[1, 3]])

    def test_remove_column_from_list_with_multiple_elements(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = remove_column(list1, 0)
        self.assertEqual(result, [[2, 3], [5, 6], [8, 9]])

    def test_remove_column_from_list_with_invalid_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            remove_column(list1, 10)
