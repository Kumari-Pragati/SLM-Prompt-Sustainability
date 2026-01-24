import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(replace_max_specialchar("", 10), "")

    def test_single_special_char(self):
        self.assertEqual(replace_max_specialchar(".", 10), ":")
        self.assertEqual(replace_max_specialchar(",", 10), ":")
        self.assertEqual(replace_max_specialchar(":", 10), ":")
        self.assertEqual(replace_max_specialchar(";", 10), ":")

    def test_multiple_special_chars(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 10), "Hello:World:")
        self.assertEqual(replace_max_specialchar("Hello., World!", 10), "Hello:World:")
        self.assertEqual(replace_max_specialchar("Hello; World!", 10), "Hello:World:")
        self.assertEqual(replace_max_specialchar("Hello., World;", 10), "Hello:World:")

    def test_max_replacement(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello, World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 2), "Hello: World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 3), "Hello:World:!")
