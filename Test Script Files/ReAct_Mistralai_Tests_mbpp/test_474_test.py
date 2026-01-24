import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):

    def test_replace_single_character(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "HeLo")

    def test_replace_multiple_characters(self):
        self.assertEqual(replace_char("Python", "h", "H"), "PytOn")

    def test_replace_empty_string(self):
        self.assertEqual(replace_char("", "a", "b"), "")

    def test_replace_nonexistent_character(self):
        self.assertEqual(replace_char("World", "x", "X"), "World")

    def test_replace_case_insensitive(self):
        self.assertEqual(replace_char("PyThOn", "t", "T"), "PyThOn")

    def test_replace_with_empty_string(self):
        self.assertEqual(replace_char("Hello", "l", ""), "H")

    def test_replace_with_none_string(self):
        with self.assertRaises(TypeError):
            replace_char("Hello", "l", None)
