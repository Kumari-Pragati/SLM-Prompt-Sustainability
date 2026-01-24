import unittest
from mbpp_628_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(replace_spaces("hello world"), "h0l0l0w0r0l0d0")
        self.assertEqual(replace_spaces(""), "")
        self.assertEqual(replace_spaces("a"), "a")

    def test_edge_cases(self):
        self.assertEqual(replace_spaces("a b"), "a0b0")
        self.assertEqual(replace_spaces("a b c"), "a0b0c0")
        self.assertEqual(replace_spaces("a b c d"), "a0b0c0d0")
        self.assertEqual(replace_spaces("a b c d e"), "a0b0c0d0e0")
        self.assertEqual(replace_spaces("a b c d e f"), "a0b0c0d0e0f0")

    def test_boundary_conditions(self):
        self.assertEqual(replace_spaces("a "), "a0")
        self.assertEqual(replace_spaces(" a "), "02%a")
        self.assertEqual(replace_spaces(" a b "), "a0b0")
        self.assertEqual(replace_spaces(" a b c "), "a0b0c0")
        self.assertEqual(replace_spaces(" a b c d "), "a0b0c0d0")
        self.assertEqual(replace_spaces(" a b c d e "), "a0b0c0d0e0")
        self.assertEqual(replace_spaces(" a b c d e f "), "a0b0c0d0e0f0")
        self.assertEqual(replace_spaces(" a b c d e f g "), "a0b0c0d0e0f0g0")

    def test_invalid_input(self):
        self.assertNotEqual(replace_spaces(123), -1)
        self.assertNotEqual(replace_spaces(None), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -1)
        self.assertNotEqual(replace_spaces(""), -