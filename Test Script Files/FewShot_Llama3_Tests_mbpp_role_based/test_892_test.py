import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_remove_single_spaces(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")

    def test_remove_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello   World"), "Hello World")

    def test_remove_spaces_at_beginning(self):
        self.assertEqual(remove_spaces("   Hello World"), "Hello World")

    def test_remove_spaces_at_end(self):
        self.assertEqual(remove_spaces("Hello World   "), "Hello World")

    def test_remove_spaces_in_middle(self):
        self.assertEqual(remove_spaces("Hello  World!"), "Hello World!")

    def test_remove_spaces_with_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_remove_spaces_with_single_space(self):
        self.assertEqual(remove_spaces(" "), "")
