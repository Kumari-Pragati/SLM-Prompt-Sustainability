import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_remove_spaces_in_string(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")

    def test_remove_multiple_spaces(self):
        self.assertEqual(remove_spaces("   Hello World   "), "Hello World")

    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_single_space_string(self):
        self.assertEqual(remove_spaces(" "), "")

    def test_spaces_at_beginning_and_end(self):
        self.assertEqual(remove_spaces(" Hello World "), "Hello World")

    def test_spaces_in_the_middle(self):
        self.assertEqual(remove_spaces("Hello World "), "HelloWorld")
