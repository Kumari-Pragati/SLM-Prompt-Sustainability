import unittest
from mbpp_800_code import remove_all_spaces

class TestRemoveAllSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_all_spaces(""), "")

    def test_single_space(self):
        self.assertEqual(remove_all_spaces("Hello World"), "HelloWorld")

    def test_multiple_spaces(self):
        self.assertEqual(remove_all_spaces("Hello   World"), "HelloWorld")

    def test_spaces_at_start_and_end(self):
        self.assertEqual(remove_all_spaces("   Hello   World   "), "HelloWorld")

    def test_no_spaces(self):
        self.assertEqual(remove_all_spaces("HelloWorld"), "HelloWorld")

    def test_spaces_and_punctuation(self):
        self.assertEqual(remove_all_spaces("Hello, World!"), "Hello,World!")
