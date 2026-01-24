import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual([], listify_list([]))

    def test_single_element_list(self):
        self.assertListEqual([[1]], listify_list([1]))

    def test_multiple_elements_list(self):
        self.assertListEqual([[1, 2], [3, 4]], listify_list([[1, 2], [3, 4]]) )

    def test_list_of_lists_with_different_lengths(self):
        self.assertListEqual([[1, 2], [3], [4, 5, 6]], listify_list([[1, 2], [3], [4, 5, 6]]) )

    def test_list_of_lists_with_empty_list(self):
        self.assertListEqual([[], [1, 2], [3]], listify_list([[], [1, 2], [3]]) )

    def test_list_of_non_list_elements(self):
        with self.assertRaises(TypeError):
            listify_list([1, 2, 3])
