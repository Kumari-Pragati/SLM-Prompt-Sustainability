import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_single_space(self):
        self.assertEqual(remove_all_spaces(" "), "")

    def test_empty_input(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_multiple_spaces(self):
        self.assertEqual(remove_all_spaces("   Hello World   "), "HelloWorld")

    def test_special_characters(self):
        self.assertEqual(remove_all_spaces("Hello World!@#$%^&*()_+-="), "HelloWorld!@#$%^&*()_+-=")

    def test_leading_trailing_spaces(self):
        self.assertEqual(remove_all_spaces("   Hello World   "), "HelloWorld")
        self.assertEqual(remove_all_spaces("Hello World   "), "HelloWorld")
        self.assertEqual(remove_all_spaces("   Hello World"), "HelloWorld")
