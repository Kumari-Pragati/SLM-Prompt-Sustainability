import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_remove_column(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        self.assertEqual(remove_column(list1, 2), expected)

    def test_remove_column_empty_list(self):
        list1 = []
        expected = []
        self.assertEqual(remove_column(list1, 0), expected)

    def test_remove_column_single_element(self):
        list1 = [[1, 2, 3]]
        expected = [[1, 2]]
        self.assertEqual(remove_column(list1, 2), expected)

    def test_remove_column_invalid_index(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            remove_column(list1, 10)
