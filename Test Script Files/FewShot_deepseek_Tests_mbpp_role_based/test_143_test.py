import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_with_list(self):
        self.assertEqual(find_lists(['a', 'b', 'c']), 1)

    def test_with_string(self):
        self.assertEqual(find_lists('abc'), 3)

    def test_with_integer(self):
        self.assertEqual(find_lists(123), 3)

    def test_with_float(self):
        self.assertEqual(find_lists(123.45), 6)

    def test_with_empty_list(self):
        self.assertEqual(find_lists([]), 0)

    def test_with_none(self):
        self.assertRaises(TypeError, find_lists, None)
