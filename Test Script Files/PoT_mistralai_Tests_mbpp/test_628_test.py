import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_spaces("hello world"), "h0l0l0w0r0l0d0w0r0l0d")
        self.assertEqual(replace_spaces(""), "")
        self.assertEqual(replace_spaces("a"), "a")
        self.assertEqual(replace_spaces("a b"), "a0b0")
        self.assertEqual(replace_spaces("a b c"), "a0b0c0")
        self.assertEqual(replace_spaces("a b c d"), "a0b0c0d0")
        self.assertEqual(replace_spaces("a b c d e"), "a0b0c0d0e0")

    def test_edge_cases(self):
        self.assertEqual(replace_spaces("a "), "a0%2")
        self.assertEqual(replace_spaces(" a "), "%200")
        self.assertEqual(replace_spaces(" a b "), "a0%2b0")
        self.assertEqual(replace_spaces(" a b c "), "a0%2b0c0")
        self.assertEqual(replace_spaces(" a b c d "), "a0%2b0c0d0")
        self.assertEqual(replace_spaces(" a b c d e "), "a0%2b0c0d0e0")
        self.assertEqual(replace_spaces("a b"), "a0b")
        self.assertEqual(replace_spaces("a b c"), "a0b0c")
        self.assertEqual(replace_spaces("a b c d"), "a0b0c0d")
        self.assertEqual(replace_spaces("a b c d e"), "a0b0c0d0e")

    def test_boundary_cases(self):
        self.assertEqual(replace_spaces("a\t"), "a0%02")
        self.assertEqual(replace_spaces("\t"), "%02")
        self.assertEqual(replace_spaces("\t a"), "%02a0")
        self.assertEqual(replace_spaces("a\n"), "a0%02")
        self.assertEqual(replace_spaces("\n"), "%02")
        self.assertEqual(replace_spaces("\na"), "%02a0")
        self.assertEqual(replace_spaces("a\r"), "a0%02")
        self.assertEqual(replace_spaces("\r"), "%02")
        self.assertEqual(replace_spaces("\ra"), "%02a0")
        self.assertEqual(replace_spaces("a " * 1001), -1)
        self.assertEqual(replace_spaces("a " * 1000), -1)
