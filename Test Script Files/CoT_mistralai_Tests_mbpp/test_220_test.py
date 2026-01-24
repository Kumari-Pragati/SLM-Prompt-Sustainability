import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(replace_max_specialchar("", 10), "")

    def test_single_character(self):
        for char in "!@#$%^&*()_+-=[]{};:'\"<>,./?":
            self.assertEqual(replace_max_specialchar(char, 10), char.replace(" ,.", ":"))

    def test_simple_string(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 10), "Hello:World:")

    def test_multiple_special_characters(self):
        self.assertEqual(replace_max_specialchar("!Hello, World.@", 10), "!Hello:World:@")

    def test_max_replacement(self):
        self.assertEqual(replace_max_specialchar("!!!Hello, World!@#$%^&*()_+-=[]{};:'\"<>,./?", 1), "!!!H:W:@#$%^&*()_+-=[]{};:'\"<>,./?:")

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            replace_max_specialchar("Test", -1)

    def test_string_with_only_special_characters(self):
        self.assertEqual(replace_max_specialchar("!@#$%^&*()_+-=[]{};:'\"<>,./?", 10), "!:@#$:%^&*:()_+-=*:{}:;:'\"<>:,./:?")
