import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):
    def test_replace_comma_and_period(self):
        self.assertEqual(replace_specialchar("Hello, World.!"), "Hello:World:!")

    def test_replace_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_replace_single_special_char(self):
        self.assertEqual(replace_specialchar("Hello,"), "Hello:")
        self.assertEqual(replace_specialchar("World."), "World:")
        self.assertEqual(replace_specialchar("!"), ":")

    def test_replace_multiple_special_chars(self):
        self.assertEqual(replace_specialchar("Hello, World.!"), "Hello:World:!")

    def test_replace_special_chars_in_middle(self):
        self.assertEqual(replace_specialchar("Hello, World"), "Hello:World")
        self.assertEqual(replace_specialchar("World."), "World:")
