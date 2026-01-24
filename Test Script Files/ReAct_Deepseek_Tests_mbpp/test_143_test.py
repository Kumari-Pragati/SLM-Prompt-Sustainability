import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):

    def test_with_list(self):
        self.assertEqual(find_lists(['a', 'b', 'c']), 1)

    def test_with_non_list(self):
        self.assertEqual(find_lists('abc'), 3)

    def test_with_empty_list(self):
        self.assertEqual(find_lists([]), 1)

    def test_with_integer(self):
        self.assertEqual(find_lists(123), 3)

    def test_with_float(self):
        self.assertEqual(find_lists(123.45), 6)

    def test_with_boolean(self):
        self.assertEqual(find_lists(True), 1)

    def test_with_none(self):
        self.assertEqual(find_lists(None), 1)
