import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(replace_char("Hello World", "o", "O"), "Hello World")
        self.assertEqual(replace_char("Hello World", "W", "w"), "Hello world")
        self.assertEqual(replace_char("Hello World", "H", "h"), "hello world")

    def test_edge_cases(self):
        self.assertEqual(replace_char("", "a", "b"), "")
        self.assertEqual(replace_char("a", "a", "b"), "b")
        self.assertEqual(replace_char("a", "b", "a"), "a")

    def test_boundary_cases(self):
        self.assertEqual(replace_char("Hello World", "o", "O", count=1), "Hello World")
        self.assertEqual(replace_char("Hello World", "o", "O", count=2), "Hello World")
        self.assertEqual(replace_char("Hello World", "o", "O", count=0), "Hello World")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            replace_char(None, "a", "b")
        with self.assertRaises(TypeError):
            replace_char("Hello World", None, "b")
        with self.assertRaises(TypeError):
            replace_char("Hello World", "a", None)
