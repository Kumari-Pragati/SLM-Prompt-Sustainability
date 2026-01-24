import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(replace_spaces(""), "")

    def test_single_space(self):
        self.assertEqual(replace_spaces(" a "), "%02x")

    def test_multiple_spaces(self):
        self.assertEqual(replace_spaces("hello world"), "%h02ell02o02 02w02o02r02d")

    def test_long_string(self):
        long_string = "a" * 1001
        with self.assertRaises(ValueError):
            replace_spaces(long_string)

    def test_max_length_with_spaces(self):
        max_string = "a" * 1000 + " "
        self.assertEqual(replace_spaces(max_string), "%h02e02r02o02 02w02o02r02d")

    def test_string_with_only_spaces(self):
        self.assertEqual(replace_spaces("   "), "%02e")

    def test_string_with_special_characters(self):
        self.assertEqual(replace_spaces("!@#$%^&*()_+-=[]{}|;':\"<>,.?/"), "!@#$%^&*()_+-=[]{}|;':\"<>,.?/")
