import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):
    def test_replace_single_blank(self):
        self.assertEqual(replace_blank("Hello World", "_"), "Hello_World")

    def test_replace_multiple_blanks(self):
        self.assertEqual(replace_blank("Hello   World", "_"), "Hello__World")

    def test_replace_no_blanks(self):
        self.assertEqual(replace_blank("Hello", "_"), "Hello")

    def test_replace_empty_string(self):
        self.assertEqual(replace_blank("", "_"), "")

    def test_replace_with_invalid_input(self):
        self.assertRaises(TypeError, replace_blank, "Hello", 123)
