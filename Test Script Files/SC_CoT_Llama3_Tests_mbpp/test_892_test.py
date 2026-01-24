import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_spaces("Hello   World"), "Hello World")

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello    World   "), "Hello World")

    def test_single_space(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")

    def test_no_spaces(self):
        self.assertEqual(remove_spaces(""), "")

    def test_single_space_at_start(self):
        self.assertEqual(remove_spaces("  Hello World"), "Hello World")

    def test_single_space_at_end(self):
        self.assertEqual(remove_spaces("Hello World  "), "Hello World")

    def test_multiple_spaces_at_start(self):
        self.assertEqual(remove_spaces("   Hello World"), "Hello World")

    def test_multiple_spaces_at_end(self):
        self.assertEqual(remove_spaces("Hello World   "), "Hello World")

    def test_spaces_in_between_words(self):
        self.assertEqual(remove_spaces("Hello  World  Again"), "Hello World Again")

    def test_spaces_in_between_words_multiple(self):
        self.assertEqual(remove_spaces("Hello  World  Again  Forever"), "Hello World Again Forever")

    def test_spaces_at_start_and_end(self):
        self.assertEqual(remove_spaces("   Hello   World   "), "Hello World")

    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")
