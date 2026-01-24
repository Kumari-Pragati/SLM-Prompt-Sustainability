import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_first_repeated_char(self):
        self.assertEqual(first_repeated_char("abc"), "a")
        self.assertEqual(first_repeated_char("aabbcc"), "a")
        self.assertEqual(first_repeated_char("abcdef"), "None")
        self.assertEqual(first_repeated_char("aaabbbcc"), "a")
        self.assertEqual(first_repeated_char("a"), "a")
        self.assertEqual(first_repeated_char(""), "None")

    def test_edge_cases(self):
        self.assertEqual(first_repeated_char("a"), "a")
        self.assertEqual(first_repeated_char(""), "None")
        self.assertEqual(first_repeated_char("a"), "a")
        self.assertEqual(first_repeated_char("a"), "a")
