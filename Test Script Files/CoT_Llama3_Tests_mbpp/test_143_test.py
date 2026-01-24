import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_list_input(self):
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_non_list_input(self):
        self.assertEqual(find_lists("Hello"), 5)

    def test_empty_list_input(self):
        self.assertEqual(find_lists([]), 1)

    def test_empty_string_input(self):
        self.assertEqual(find_lists(""), 0)

    def test_tuple_input(self):
        self.assertEqual(find_lists((1, 2, 3)), 1)

    def test_dict_input(self):
        self.assertEqual(find_lists({"a": 1, "b": 2}), 1)

    def test_set_input(self):
        self.assertEqual(find_lists({1, 2, 3}), 1)

    def test_list_of_lists_input(self):
        self.assertEqual(find_lists([[1, 2, 3], [4, 5, 6]]), 1)
