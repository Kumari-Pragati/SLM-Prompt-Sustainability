import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_replace_single_char(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "HeLo")

    def test_replace_multiple_chars(self):
        self.assertEqual(replace_char("Python", "h", "H"), "PYhtOn")

    def test_replace_empty_string(self):
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_replace_case_insensitive(self):
        self.assertEqual(replace_char("PyThOn", "p", "P"), "PyTHOn")

    def test_replace_non_existent_char(self):
        self.assertEqual(replace_char("Hello", "z", "Z"), "Hello")

    def test_replace_with_empty_string(self):
        self.assertEqual(replace_char("Hello", "l", ""), "H")
