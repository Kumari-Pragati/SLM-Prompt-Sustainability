import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(replace_specialchar(""), "")

    def test_single_char(self):
        self.assertEqual(replace_specialchar("a"), "a")
        self.assertEqual(replace_specialchar("A"), "A")
        self.assertEqual(replace_specialchar("0"), "0")

    def test_single_special_char(self):
        self.assertEqual(replace_specialchar(","), ":")
        self.assertEqual(replace_specialchar("."), ":")
        self.assertEqual(replace_specialchar(" "), ":")

    def test_multiple_special_chars(self):
        self.assertEqual(replace_specialchar(",., "), "::")
        self.assertEqual(replace_specialchar(" .,  "), "::")
        self.assertEqual(replace_specialchar(" ,.  "), "::")

    def test_special_chars_in_middle(self):
        self.assertEqual(replace_specialchar("Hello, World."), "Hello:World:")
        self.assertEqual(replace_specialchar("Hello World."), "Hello:World:")
        self.assertEqual(replace_specialchar("Hello World,!"), "Hello:World:")

    def test_special_chars_at_beginning_and_end(self):
        self.assertEqual(replace_specialchar(",Hello, World."), ":Hello:World:")
        self.assertEqual(replace_specialchar("Hello, World.,",), ":Hello:World:")
        self.assertEqual(replace_specialchar(".,Hello, World.",), ":Hello:World:")
