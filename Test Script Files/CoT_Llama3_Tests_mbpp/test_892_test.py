import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_spaces("Hello   World"), "Hello World")

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello    World"), "Hello World")

    def test_single_space(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")

    def test_no_spaces(self):
        self.assertEqual(remove_spaces("HelloWorld"), "HelloWorld")

    def test_leading_spaces(self):
        self.assertEqual(remove_spaces("   Hello World"), "Hello World")

    def test_trailing_spaces(self):
        self.assertEqual(remove_spaces("Hello World   "), "Hello World")

    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_single_space_input(self):
        self.assertEqual(remove_spaces("Hello"), "Hello")

    def test_multiple_spaces_input(self):
        self.assertEqual(remove_spaces("Hello    World"), "Hello World")
