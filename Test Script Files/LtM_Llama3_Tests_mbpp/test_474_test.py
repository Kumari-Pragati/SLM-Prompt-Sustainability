import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(replace_char("hello", "o", "a"), "hella")

    def test_empty_string(self):
        self.assertEqual(replace_char("", "o", "a"), "")

    def test_no_replacement(self):
        self.assertEqual(replace_char("hello", "z", "a"), "hello")

    def test_replace_all(self):
        self.assertEqual(replace_char("hello", "o", "x"), "hxllx")

    def test_replace_first(self):
        self.assertEqual(replace_char("hello", "o", "a"), "hala")

    def test_replace_last(self):
        self.assertEqual(replace_char("hello", "o", "a"), "hellaa")

    def test_replace_middle(self):
        self.assertEqual(replace_char("hello", "l", "a"), "haoa")

    def test_replace_all_chars(self):
        self.assertEqual(replace_char("hello", "h", "a"), "alao")

    def test_replace_all_chars_to_empty(self):
        self.assertEqual(replace_char("hello", "h", ""), "ello")
