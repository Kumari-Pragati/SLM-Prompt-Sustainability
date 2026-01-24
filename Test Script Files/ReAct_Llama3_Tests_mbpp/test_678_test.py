import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_string_with_spaces(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")

    def test_string_with_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello   World"), "HelloWorld")

    def test_string_with_leading_spaces(self):
        self.assertEqual(remove_spaces("   Hello World"), "HelloWorld")

    def test_string_with_trailing_spaces(self):
        self.assertEqual(remove_spaces("Hello World   "), "HelloWorld")

    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces("HelloWorld"), "HelloWorld")

    def test_string_with_non_space_characters(self):
        self.assertEqual(remove_spaces("Hello!World"), "Hello!World")

    def test_string_with_spaces_and_non_space_characters(self):
        self.assertEqual(remove_spaces("Hello World!"), "HelloWorld!")
