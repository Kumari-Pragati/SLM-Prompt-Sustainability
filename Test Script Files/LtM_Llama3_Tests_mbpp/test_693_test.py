import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_multiple_spaces("Hello   World"), "Hello World")

    def test_edge_empty(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_edge_single_space(self):
        self.assertEqual(remove_multiple_spaces("Hello World"), "Hello World")

    def test_edge_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello   World   "), "Hello World")

    def test_edge_leading_spaces(self):
        self.assertEqual(remove_multiple_spaces("   Hello World"), "Hello World")

    def test_edge_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello World   "), "Hello World")

    def test_edge_mixed_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello   World  !"), "Hello World!")

    def test_edge_multiple_spaces_with_punctuation(self):
        self.assertEqual(remove_multiple_spaces("Hello   World,!"), "Hello World,!")
