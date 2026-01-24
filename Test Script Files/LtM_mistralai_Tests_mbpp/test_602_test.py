import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_simple_single_char(self):
        self.assertEqual(first_repeated_char("a"), "a")
        self.assertEqual(first_repeated_char("b"), "b")
        self.assertEqual(first_repeated_char("c"), "c")

    def test_simple_multiple_chars(self):
        self.assertEqual(first_repeated_char("aa"), "a")
        self.assertEqual(first_repeated_char("bb"), "b")
        self.assertEqual(first_repeated_char("cc"), "c")

    def test_edge_single_char(self):
        self.assertEqual(first_repeated_char(""), "None")
        self.assertEqual(first_repeated_char(" "), "None")
        self.assertEqual(first_repeated_char("a "), "None")
        self.assertEqual(first_repeated_char(" a"), "None")
        self.assertEqual(first_repeated_char(" aa"), "a")
        self.assertEqual(first_repeated_char(" aa "), "None")

    def test_edge_multiple_chars(self):
        self.assertEqual(first_repeated_char("ab"), "None")
        self.assertEqual(first_repeated_char("abab"), "b")
        self.assertEqual(first_repeated_char("abcd"), "None")
        self.assertEqual(first_repeated_char("abcdabcd"), "d")
        self.assertEqual(first_repeated_char("abcdabcdabcd"), "c")
