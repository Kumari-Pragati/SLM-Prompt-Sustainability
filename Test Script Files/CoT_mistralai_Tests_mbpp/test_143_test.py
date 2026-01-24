import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_lists([]), 0)

    def test_single_element_list(self):
        self.assertEqual(find_lists([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(find_lists([1, 2, 3]), 3)

    def test_list_with_different_types(self):
        self.assertEqual(find_lists([1, 2, "3"]), 3)

    def test_list_with_nested_lists(self):
        self.assertEqual(find_lists([[1, 2], [3, 4]]), 4)

    def test_list_with_none(self):
        self.assertEqual(find_lists([None]), 1)

    def test_list_with_empty_string(self):
        self.assertEqual(find_lists([""]), 0)

    def test_list_with_empty_tuple(self):
        self.assertEqual(find_lists((1,)), 1)

    def test_list_with_empty_set(self):
        self.assertEqual(find_lists({1}), 1)

    def test_list_with_empty_dict(self):
        self.assertEqual(find_lists({1: 2}), 2)

    def test_list_with_non_iterable_input(self):
        self.assertRaises(TypeError, find_lists, 1)
