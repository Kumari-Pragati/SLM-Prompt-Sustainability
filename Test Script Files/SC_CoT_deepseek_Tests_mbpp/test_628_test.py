import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_spaces("Hello World"), "Hello%20World")

    def test_edge_case(self):
        self.assertEqual(replace_spaces(" "), "%20")

    def test_boundary_case(self):
        self.assertEqual(replace_spaces("a" * 1000), "a" * 1000)
        self.assertEqual(replace_spaces("a" * 1001), -1)

    def test_special_case(self):
        self.assertEqual(replace_spaces(""), "")
        self.assertEqual(replace_spaces("a b c"), "a%20b%20c")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_spaces(123)
