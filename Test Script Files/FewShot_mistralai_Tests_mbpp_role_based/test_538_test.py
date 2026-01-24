import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_single_item_list(self):
        self.assertEqual(string_list_to_tuple(["a"]), ("a",))

    def test_multiple_items_list(self):
        self.assertEqual(string_list_to_tuple(["a", "b", "c"]), ("a", "b", "c"))

    def test_list_with_spaces(self):
        self.assertEqual(string_list_to_tuple(["a", " ", "b"]), ("a", "b"))

    def test_list_with_only_spaces(self):
        self.assertEqual(string_list_to_tuple([" ", " ", " "]), ())
