import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_simple_non_list(self):
        self.assertEqual(find_lists("hello"), 5)

    def test_empty_list(self):
        self.assertEqual(find_lists([]), 1)

    def test_empty_non_list(self):
        self.assertEqual(find_lists(""), 0)

    def test_list_of_lists(self):
        self.assertEqual(find_lists([[], [1, 2], [3, 4]]), 1)

    def test_non_list_of_lists(self):
        self.assertEqual(find_lists(["hello", [1, 2], [3, 4]]), 3)
