import unittest
from mbpp_857_code import listify_list

class TestListifyList(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(listify_list([]), [[]])

    def test_single_element_list(self):
        self.assertListEqual(listify_list([1]), [[1]])

    def test_multiple_elements_list(self):
        self.assertListEqual(listify_list([1, 2, 3]), [[1], [2], [3]])

    def test_list_with_mixed_types(self):
        self.assertListEqual(listify_list([1, "hello", 3.14]), [[1], ["hello"], [3.14]])

    def test_list_with_nested_lists(self):
        self.assertListEqual(listify_list([[1, 2], [3, 4]]), [[[1, 2]], [[3, 4]]])
