import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_typical_list(self):
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_typical_non_list(self):
        self.assertEqual(find_lists("hello"), 5)

    def test_edge_list_empty(self):
        self.assertEqual(find_lists([]), 1)

    def test_edge_list_single_element(self):
        self.assertEqual(find_lists([1]), 1)

    def test_edge_list_multiple_elements(self):
        self.assertEqual(find_lists([1, 2, 3, 4, 5]), 1)

    def test_edge_non_list_empty(self):
        self.assertEqual(find_lists(""), 0)

    def test_edge_non_list_single_element(self):
        self.assertEqual(find_lists("a"), 1)

    def test_edge_non_list_multiple_elements(self):
        self.assertEqual(find_lists("abc"), 3)

    def test_corner_list_nested(self):
        self.assertEqual(find_lists([1, [2, 3]]), 1)

    def test_corner_non_list_nested(self):
        self.assertEqual(find_lists({"a": "b", "c": "d"}), 2)
