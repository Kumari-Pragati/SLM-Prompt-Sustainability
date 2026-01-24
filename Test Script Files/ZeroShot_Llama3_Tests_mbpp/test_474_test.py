import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_replace_char(self):
        self.assertEqual(replace_char("Hello, World!", ",", "."), "Hello. World!")
        self.assertEqual(replace_char("Hello, World!", " ", "_"), "Hello_World!")
        self.assertEqual(replace_char("Hello, World!", "o", "0"), "Hell0, World!")
        self.assertEqual(replace_char("Hello, World!", "a", "A"), "Hell0, World!")
        self.assertEqual(replace_char("Hello, World!", "z", "Z"), "Hell0, World!")
        self.assertEqual(replace_char("Hello, World!", "!", "!"), "Hello, World!")
        self.assertEqual(replace_char("Hello, World!", " ", ""), "Hello,World!")
        self.assertEqual(replace_char("Hello, World!", " ", "  "), "Hello, World!")
        self.assertEqual(replace_char("Hello, World!", " ", "   "), "Hello, World!")

    def test_replace_char_empty_string(self):
        self.assertEqual(replace_char("", "a", "A"), "")

    def test_replace_char_no_change(self):
        self.assertEqual(replace_char("Hello, World!", "x", "x"), "Hello, World!")

    def test_replace_char_multiple_chars(self):
        self.assertEqual(replace_char("Hello, World!", "o", "0"), "Hell0, World!")
        self.assertEqual(replace_char("Hello, World!", "o", "0", 1), "Hell0, World!")
