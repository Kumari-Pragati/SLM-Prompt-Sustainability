import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_remove_spaces_from_string(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")

    def test_remove_spaces_from_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_remove_spaces_from_string_with_multiple_spaces(self):
        self.assertEqual(remove_spaces("   Hello   World   "), "HelloWorld")

    def test_remove_spaces_from_string_with_leading_spaces(self):
        self.assertEqual(remove_spaces("   Hello World"), "HelloWorld")

    def test_remove_spaces_from_string_with_trailing_spaces(self):
        self.assertEqual(remove_spaces("Hello World   "), "HelloWorld")
