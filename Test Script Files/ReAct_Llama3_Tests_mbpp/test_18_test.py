import unittest
from mbpp_18_code import remove_dirty_chars

class TestRemoveDirtyChars(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "World"), "Hello, ")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_dirty_chars("", "abc"), "")

    def test_edge_case_empty_second_string(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", ""), "Hello, World!")

    def test_edge_case_no_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "Hello, World!"), "Hello, World!")

    def test_edge_case_no_characters_to_remove(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "xyz"), "Hello, World!")

    def test_edge_case_all_characters_to_remove(self):
        self.assertEqual(remove_dirty_chars("Hello, World!", "Hello, World!abc"), "")

    def test_edge_case_multiple_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("Hello, World!abc, def", "abc, def"), "Hello, World!")

    def test_edge_case_dirty_chars_in_middle(self):
        self.assertEqual(remove_dirty_chars("Hello, World!abc, def, ghi", "abc, def"), "Hello, World!ghi")

    def test_edge_case_dirty_chars_at_beginning(self):
        self.assertEqual(remove_dirty_chars("abc, def, ghi Hello, World!", "abc, def"), "ghi Hello, World!")

    def test_edge_case_dirty_chars_at_end(self):
        self.assertEqual(remove_dirty_chars("Hello, World!abc, def, ghi", "abc, def"), "Hello, World!ghi")
