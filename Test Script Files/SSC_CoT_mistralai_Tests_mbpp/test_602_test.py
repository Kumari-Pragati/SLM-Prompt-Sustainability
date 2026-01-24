import unittest
from mbpp_602_code import OrderedDict

from 602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(first_repeated_char("abcabc"), "a")
        self.assertEqual(first_repeated_char("aabbc"), "a")
        self.assertEqual(first_repeated_char("aaa"), "a")
        self.assertEqual(first_repeated_char(""), "None")
        self.assertEqual(first_repeated_char("abc"), "None")
        self.assertEqual(first_repeated_char("abcd"), "None")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_repeated_char("a"), "None")
        self.assertEqual(first_repeated_char("aa"), "a")
        self.assertEqual(first_repeated_char("aabbcc"), "a")
        self.assertEqual(first_repeated_char("a" * 1000), "a")
        self.assertEqual(first_repeated_char("A" * 1000), "None")
        self.assertEqual(first_repeated_char("0123456789"), "None")
        self.assertEqual(first_repeated_char("!@#$%^&*()_+-=[]{}|;:'\",.<>?/"), "None")

    def test_special_or_corner_cases(self):
        self.assertEqual(first_repeated_char("aaa\nb"), "a")
        self.assertEqual(first_repeated_char("aaa\r\nb"), "a")
        self.assertEqual(first_repeated_char("aaa\t\nb"), "a")
        self.assertEqual(first_repeated_char("aaa\n\nb"), "a")
        self.assertEqual(first_repeated_char("aaa\n\r\nb"), "a")
        self.assertEqual(first_repeated_char("aaa\n\t\r\nb"), "a")
        self.assertEqual(first_repeated_char("aaa\n\t\r\n\b"), "None")
