import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(find_lists(['a', 'b', 'c']), 1)

    def test_non_list_input(self):
        self.assertEqual(find_lists('abc'), 3)
        self.assertEqual(find_lists(123), 3)
        self.assertEqual(find_lists({'a': 1, 'b': 2}), 2)

    def test_empty_input(self):
        self.assertEqual(find_lists(''), 0)
        self.assertEqual(find_lists([]), 1)

    def test_list_with_one_element(self):
        self.assertEqual(find_lists(['a']), 1)
