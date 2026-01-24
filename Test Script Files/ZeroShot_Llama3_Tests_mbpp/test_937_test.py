import unittest
from mbpp_937_code import max_char

class TestMaxChar(unittest.TestCase):

    def test_max_char(self):
        self.assertEqual(max_char("hello"), 'l')
        self.assertEqual(max_char("world"), 'r')
        self.assertEqual(max_char("python"), 't')
        self.assertEqual(max_char("unittest"), 't')
        self.assertEqual(max_char("abcdefghijklmnopqrstuvwxyz"), 'z')
        self.assertEqual(max_char("1234567890"), '0')
        self.assertEqual(max_char("abcabcabc"), 'a')
        self.assertEqual(max_char("a"), 'a')
        self.assertEqual(max_char(""), None)

    def test_max_char_edge_cases(self):
        self.assertEqual(max_char("a"*1000), 'a')
        self.assertEqual(max_char("a"*1000 + "b"*1000), 'a')
