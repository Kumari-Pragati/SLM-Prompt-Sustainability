import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):

    def test_with_list(self):
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_with_non_list(self):
        self.assertEqual(find_lists("123"), 3)

    def test_with_empty_list(self):
        self.assertEqual(find_lists([]), 1)

    def test_with_None(self):
        self.assertEqual(find_lists(None), 0)

    def test_with_integer(self):
        self.assertEqual(find_lists(123), 3)

    def test_with_float(self):
        self.assertEqual(find_lists(123.45), 6)

    def test_with_boolean(self):
        self.assertEqual(find_lists(True), 4)

    def test_with_complex(self):
        self.assertEqual(find_lists(1 + 2j), 5)

    def test_with_dict(self):
        self.assertEqual(find_lists({}), 0)

    def test_with_set(self):
        self.assertEqual(find_lists({1, 2, 3}), 1)
