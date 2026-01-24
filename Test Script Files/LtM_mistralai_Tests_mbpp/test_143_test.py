import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_empty_list(self):
        self.assertEqual(find_lists([]), 0)

    def test_single_element_list(self):
        self.assertEqual(find_lists([4]), 1)

    def test_string_input(self):
        self.assertEqual(find_lists('test'), len('test'))

    def test_tuple_input(self):
        self.assertEqual(find_lists((1, 2, 3)), len((1, 2, 3)))

    def test_set_input(self):
        self.assertEqual(find_lists({1, 2, 3}), len({1, 2, 3}))

    def test_dict_input(self):
        self.assertEqual(find_lists({'a': 1, 'b': 2}), len({'a': 1, 'b': 2}))
