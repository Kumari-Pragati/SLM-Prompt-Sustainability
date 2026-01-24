import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(replace_char("Hello, World!", ",", "."), "Hello.. World!")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_edge_case_single_character_string(self):
        self.assertEqual(replace_char("a", "a", "b"), "b")

    def test_edge_case_no_replacement(self):
        self.assertEqual(replace_char("Hello, World!", "x", "x"), "Hello, World!")

    def test_edge_case_replacement_with_no_change(self):
        self.assertEqual(replace_char("Hello, World!", " ", " "), "Hello, World!")

    def test_edge_case_replacement_with_change(self):
        self.assertEqual(replace_char("Hello, World!", "o", "O"), "HellO, World!")

    def test_edge_case_replacement_with_multiple_chars(self):
        self.assertEqual(replace_char("Hello, World!", "o", "OO"), "HellOO, World!")
