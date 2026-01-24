import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_listify_list_with_empty_list(self):
        self.assertEqual(listify_list([]), [])

    def test_listify_list_with_single_element(self):
        self.assertEqual(listify_list([1]), [[1]])

    def test_listify_list_with_multiple_elements(self):
        self.assertEqual(listify_list([1, 2, 3]), [[1], [2], [3]])

    def test_listify_list_with_nested_list(self):
        self.assertEqual(listify_list([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_listify_list_with_mixed_elements(self):
        self.assertEqual(listify_list([1, 'a', [3, 4]]), [[1], ['a'], [[3], [4]]])
