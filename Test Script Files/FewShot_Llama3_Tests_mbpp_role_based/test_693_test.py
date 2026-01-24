import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_multiple_spaces("Hello   World"), "Hello World")

    def test_single_space(self):
        self.assertEqual(remove_multiple_spaces("Hello World"), "Hello World")

    def test_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello    World    "), "Hello World")

    def test_leading_spaces(self):
        self.assertEqual(remove_multiple_spaces("   Hello World"), "Hello World")

    def test_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello World   "), "Hello World")

    def test_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")
