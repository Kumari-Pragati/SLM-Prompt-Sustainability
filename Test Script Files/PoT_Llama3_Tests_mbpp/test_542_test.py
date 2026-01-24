import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:, world:")
        self.assertEqual(fill_spaces("This is a test"), "This:, is:, a:, test")

    def test_edge(self):
        self.assertEqual(fill_spaces(""), "")
        self.assertEqual(fill_spaces("Hello"), "Hello")

    def test_corner(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:, world:")
        self.assertEqual(fill_spaces("Hello, world..."), "Hello:, world:")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            fill_spaces(123)
