import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_spaces("Hello   World"), "Hello World")
        self.assertEqual(remove_spaces("   Hello   World   "), "Hello World")
        self.assertEqual(remove_spaces("Hello   World   "), "Hello World")

    def test_edge(self):
        self.assertEqual(remove_spaces(""), "")
        self.assertEqual(remove_spaces("   "), " ")
        self.assertEqual(remove_spaces("   Hello   "), "Hello")

    def test_corner(self):
        self.assertEqual(remove_spaces("Hello   World  !"), "Hello World!")
        self.assertEqual(remove_spaces("   Hello   World  !   "), "Hello World!")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_spaces(123)
