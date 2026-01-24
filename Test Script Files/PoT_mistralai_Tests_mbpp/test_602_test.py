import unittest
from mbpp_602_code import deque

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_repeated_char("hello"), "l")
        self.assertEqual(first_repeated_char("leetcode"), "e")
        self.assertEqual(first_repeated_Char("aabbcc"), "a")

    def test_edge_cases(self):
        self.assertEqual(first_repeated_char(""), "None")
        self.assertEqual(first_repeated_char("a"), "a")
        self.assertEqual(first_repeated_char("aa"), "a")
        self.assertEqual(first_repeated_char("aaa"), "a")
        self.assertEqual(first_repeated_char("abcd"), "None")
        self.assertEqual(first_repeated_char("abcdefghijklmnopqrstuvwxyz"), "a")

    def test_corner_cases(self):
        self.assertEqual(first_repeated_char("aaaabbbbcccc"), "a")
        self.assertEqual(first_repeated_char("aabbccddaa"), "a")
        self.assertEqual(first_repeated_char("aabbccdd"), "None")
        self.assertEqual(first_repeated_char("AABBCCdd"), "A")
        self.assertEqual(first_repeated_char("1234567890"), "1")
        self.assertEqual(first_repeated_char("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), "!")
