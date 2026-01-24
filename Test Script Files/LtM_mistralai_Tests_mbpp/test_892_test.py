import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")
        self.assertEqual(remove_spaces("  Hello World  "), "Hello World")

    def test_edge_input(self):
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("Hello"), "Hello")
        self.assertEqual(remove_spaces("Hello World!"), "Hello World!")

    def test_boundary_input(self):
        self.assertEqual(remove_spaces("Hello   World"), "Hello World")
        self.assertEqual(remove_spaces("Hello World  "), "Hello World")
        self.assertEqual(remove_spaces("Hello World!"), "Hello World!")

    def test_complex_input(self):
        self.assertEqual(remove_spaces("Hello World!   How are you?"), "Hello World! How are you?")
        self.assertEqual(remove_spaces("Hello World!   How   are   you?"), "Hello World! How are you")
