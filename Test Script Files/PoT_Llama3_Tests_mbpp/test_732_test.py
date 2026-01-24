import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialchar(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")
        self.assertEqual(replace_specialchar("This is a test."), "This: is: a: test.")
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")

    def test_edge(self):
        self.assertEqual(replace_specialchar(""), "")
        self.assertEqual(replace_specialchar("Hello"), "Hello")

    def test_corner(self):
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            replace_specialchar(123)
