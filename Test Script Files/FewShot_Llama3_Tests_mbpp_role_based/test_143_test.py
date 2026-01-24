import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_list_input(self):
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_non_list_input(self):
        self.assertEqual(find_lists("Hello, World!"), 11)

    def test_empty_list_input(self):
        self.assertEqual(find_lists([]), 1)

    def test_nested_list_input(self):
        self.assertEqual(find_lists([1, [2, 3]]), 1)

    def test_mixed_input(self):
        self.assertEqual(find_lists([1, "Hello", 3]), 1)
