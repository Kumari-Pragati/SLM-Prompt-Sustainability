import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(first_repeated_char("abcabc"), 'a')

    def test_edge_case(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case2(self):
        self.assertEqual(first_repeated_char("abc"), 'None')

    def test_edge_case3(self):
        self.assertEqual(first_repeated_char(""), 'None')

    def test_edge_case4(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case5(self):
        self.assertEqual(first_repeated_char("abcdef"), 'a')

    def test_edge_case6(self):
        self.assertEqual(first_repeated_char("aabbcc"), 'a')

    def test_edge_case7(self):
        self.assertEqual(first_repeated_char("abcdeff"), 'f')

    def test_edge_case8(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case9(self):
        self.assertEqual(first_repeated_char("ab"), 'None')

    def test_edge_case10(self):
        self.assertEqual(first_repeated_char("abc"), 'None')

    def test_edge_case11(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case12(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case13(self):
        self.assertEqual(first_repeated_char("abc"), 'None')

    def test_edge_case14(self):
        self.assertEqual(first_repeated_char("abc"), 'None')

    def test_edge_case15(self):
        self.assertEqual(first_repeated_char("abc"), 'None')

    def test_edge_case16(self):
        self.assertEqual(first_repeated_char("abc"), 'None')
