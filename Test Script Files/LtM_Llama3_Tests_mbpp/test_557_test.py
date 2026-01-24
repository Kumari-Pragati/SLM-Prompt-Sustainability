import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_simple_strings(self):
        self.assertEqual(toggle_string("Hello"), "hELLO")
        self.assertEqual(toggle_string("hello"), "HELLO")
        self.assertEqual(toggle_string("123"), "123")

    def test_edge_cases(self):
        self.assertEqual(toggle_string(""), "")
        self.assertEqual(toggle_string("a"), "A")
        self.assertEqual(toggle_string("ABC"), "abc")

    def test_toggle_all_chars(self):
        self.assertEqual(toggle_string("abcdefghijklmnopqrstuvwxyz"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(toggle_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "abcdefghijklmnopqrstuvwxyz")

    def test_toggle_string_with_spaces(self):
        self.assertEqual(toggle_string("Hello World"), "hELLO wORLD")
