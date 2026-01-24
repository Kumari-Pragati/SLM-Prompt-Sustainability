import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_column([], 0), [])

    def test_single_element_list(self):
        self.assertListEqual(remove_column([1, 2, 3], 1), [1, 3])

    def test_list_with_one_deleted_element(self):
        self.assertListEqual(remove_column([1, 2, 3], 1), [1, 3])

    def test_list_with_multiple_deleted_elements(self):
        self.assertListEqual(remove_column([1, 2, 3, 4, 5], 1), [1, 4, 5])

    def test_list_with_negative_index(self):
        self.assertListEqual(remove_column([1, 2, 3], -1), [1, 2])

    def test_list_with_index_greater_than_length(self):
        self.assertListEqual(remove_column([1, 2, 3], 3), [1, 2])
