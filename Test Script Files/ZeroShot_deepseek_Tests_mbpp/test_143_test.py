import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):

    def test_find_lists_with_list(self):
        self.assertEqual(find_lists(['a', 'b', 'c']), 1)

    def test_find_lists_with_string(self):
        self.assertEqual(find_lists('abc'), 3)

    def test_find_lists_with_integer(self):
        self.assertEqual(find_lists(123), 3)

    def test_find_lists_with_float(self):
        self.assertEqual(find_lists(12.3), 4)

    def test_find_lists_with_boolean(self):
        self.assertEqual(find_lists(True), 1)

    def test_find_lists_with_none(self):
        self.assertEqual(find_lists(None), 1)
