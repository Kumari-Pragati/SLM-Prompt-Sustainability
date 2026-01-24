import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(replace_max_specialchar("", 10), "")

    def test_single_character(self):
        for char in "!@#$%^&*()_+-=[]{};:'\",.<>?/":
            self.assertEqual(replace_max_specialchar(char, 10), char.replace(",.", ":"))

    def test_special_characters_only(self):
        test_str = "!@#$%^&*()_+-=[]{};:'\",.<>?/ "
        self.assertEqual(replace_max_specialchar(test_str, 10), test_str.replace(",.", ":") * 10)

    def test_normal_string(self):
        test_str = "Hello, World! It's a nice day, isn't it?"
        expected_str = "Hello:World! It's a nice day, isn't it:"
        self.assertEqual(replace_max_specialchar(test_str, 1), expected_str)
        self.assertEqual(replace_max_specialchar(test_str, 10), expected_str * 10)

    def test_long_string(self):
        test_str = "a" * 1000 + ", World!"
        expected_str = "a" * 1000 + ":World!"
        self.assertEqual(replace_max_specialchar(test_str, 1), expected_str)
        self.assertEqual(replace_max_specialchar(test_str, 10), expected_str * 10)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            replace_max_specialchar("test", -1)
