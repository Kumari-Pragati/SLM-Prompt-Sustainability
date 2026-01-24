import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_column([], 0), [])

    def test_single_element_list(self):
        self.assertListEqual(remove_column([1, 2, 3], 0), [2, 3])
        self.assertListEqual(remove_column([1, 2, 3], 1), [1, 3])
        self.assertListEqual(remove_column([1, 2, 3], 2), [1, 2])

    def test_multiple_elements_list(self):
        self.assertListEqual(remove_column([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1),
                             [[1, None, 3], [4, None, 6], [7, None, 9]])

    def test_negative_index(self):
        self.assertListEqual(remove_column([1, 2, 3], -1), [1, 2, 3])
        self.assertListEqual(remove_column([1, 2, 3], -2), [1, None, 3])

    def test_invalid_index(self):
        self.assertRaises(IndexError, remove_column, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4)

    def test_list_with_non_list_elements(self):
        self.assertRaises(TypeError, remove_column, [1, 'a', [2, 3]], 1)
