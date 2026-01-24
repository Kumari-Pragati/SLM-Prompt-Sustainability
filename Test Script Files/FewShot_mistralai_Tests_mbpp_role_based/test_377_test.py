import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_Char("", "a"), "")

    def test_single_char_string(self):
        self.assertEqual(remove_Char("a", "a"), "")
        self.assertEqual(remove_Char("b", "a"), "b")

    def test_multiple_chars_string(self):
        self.assertEqual(remove_Char("aaa", "a"), "")
        self.assertEqual(remove_Char("bbb", "b"), "")
        self.assertEqual(remove_Char("aba", "a"), "b")
        self.assertEqual(remove_Char("bba", "b"), "a")

    def test_single_char_list(self):
        self.assertEqual(remove_Char(["a"], "a"), [])
        self.assertEqual(remove_Char(["b"], "a"), ["b"])

    def test_multiple_chars_list(self):
        self.assertEqual(remove_Char(["a", "a", "a"], "a"), [])
        self.assertEqual(remove_Char(["b", "b", "b"], "b"), [])
        self.assertEqual(remove_Char(["a", "b", "a"], "a"), ["b"])
        self.assertEqual(remove_Char(["b", "a", "b"], "b"), ["a"])
