import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_lists([]), 0)

    def test_single_element_list(self):
        self.assertEqual(find_lists([1]), 1)

    def test_multi_element_list(self):
        self.assertEqual(find_lists([1, 2, 3]), 3)

    def test_string_input(self):
        self.assertEqual(find_lists("test"), 4)

    def test_tuple_input(self):
        self.assertEqual(find_lists((1, 2, 3)), 3)

    def test_set_input(self):
        self.assertEqual(find_lists({1, 2, 3}), 3)

    def test_dict_input(self):
        self.assertEqual(find_lists({"key": 1, "value": 2}), 2)

    def test_list_of_lists(self):
        self.assertEqual(find_lists([[1, 2, 3], [4, 5, 6]]), 6)
