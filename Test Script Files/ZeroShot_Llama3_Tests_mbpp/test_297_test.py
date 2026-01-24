import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(flatten_list([1]), [1])

    def test_nested_list(self):
        self.assertEqual(flatten_list([1, [2, 3], 4, [5, [6, 7]]]), [1, 2, 3, 4, 5, 6, 7])

    def test_multiple_nested_lists(self):
        self.assertEqual(flatten_list([1, [2, [3, [4, [5, [6, 7]]]]]]), [1, 2, 3, 4, 5, 6, 7])

    def test_list_with_non_list_elements(self):
        self.assertEqual(flatten_list([1, 2, 3, [4, 5], 6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_list_with_empty_sublist(self):
        self.assertEqual(flatten_list([1, [2, 3], 4, [], 5, [6, 7]]), [1, 2, 3, 4, 5, 6, 7])
