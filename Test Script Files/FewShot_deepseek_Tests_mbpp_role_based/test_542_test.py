import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(fill_spaces("Hello, World!"), "Hello:World:")

    def test_edge_condition(self):
        self.assertEqual(fill_spaces(""), "")

    def test_boundary_condition(self):
        self.assertEqual(fill_spaces("Space at the beginning "), "Space at the beginning:")
        self.assertEqual(fill_spaces(" Space at the end"), ":Space at the end")
        self.assertEqual(fill_spaces(" Spaces at both ends "), " Spaces at both ends:")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fill_spaces(123)
