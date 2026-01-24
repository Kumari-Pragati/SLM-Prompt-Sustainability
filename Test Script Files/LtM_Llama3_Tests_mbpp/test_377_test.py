import unittest
from mbpp_377_code import remove_Char

class TestRemoveChar(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_Char("hello", "l"), "hoe")
        self.assertEqual(remove_Char("hello", "o"), "hell")
        self.assertEqual(remove_Char("hello", "h"), "ello")
        self.assertEqual(remove_Char("hello", "e"), "hlllo")
        self.assertEqual(remove_Char("hello", "d"), "hello")

    def test_edge(self):
        self.assertEqual(remove_Char("", "a"), "")
        self.assertEqual(remove_Char("a", "a"), "")
        self.assertEqual(remove_Char("a", "b"), "a")
        self.assertEqual(remove_Char("abc", "b"), "ac")
        self.assertEqual(remove_Char("abc", "d"), "abc")

    def test_complex(self):
        self.assertEqual(remove_Char("hello world", "o"), "hell wrld")
        self.assertEqual(remove_Char("hello world", "l"), "heo wrd")
        self.assertEqual(remove_Char("hello world", "d"), "hello world")
        self.assertEqual(remove_Char("hello world", "z"), "hello world")
