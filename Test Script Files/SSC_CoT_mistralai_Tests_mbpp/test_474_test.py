import unittest
from mbpp_474_code import replace_char

class TestReplaceChar(unittest.TestCase):
    def test_replace_normal(self):
        self.assertEqual(replace_char("Hello", "l", "L"), "HeLo")
        self.assertEqual(replace_char("Python", "h", "H"), "PyThOn")

    def test_replace_edge_cases(self):
        self.assertEqual(replace_char("", "a", "z"), "")
        self.assertEqual(replace_char("abc", "c", "z"), "azb")
        self.assertEqual(replace_char("abc", "a", "z"), "bc")
        self.assertEqual(replace_char("abc", "z", "a"), "abc")

    def test_replace_empty_char(self):
        self.assertEqual(replace_char("Hello", "", "z"), "Hello")
        self.assertEqual(replace_char("", "", "z"), "")

    def test_replace_non_string_input(self):
        self.assertRaises(TypeError, replace_char, 123, "a", "b")
        self.assertRaises(TypeError, replace_char, "abc", 123, "b")
        self.assertRaises(TypeError, replace_char, "abc", "a", 123)
