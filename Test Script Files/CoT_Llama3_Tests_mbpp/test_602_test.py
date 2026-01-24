import unittest
from mbpp_602_code import first_repeated_char

class TestFirstRepeatedChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_repeated_char("abcabc"), 'a')

    def test_edge_case(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case2(self):
        self.assertEqual(first_repeated_char("aabb"), 'a')

    def test_edge_case3(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case4(self):
        self.assertEqual(first_repeated_char("abc"), 'None')

    def test_edge_case5(self):
        self.assertEqual(first_repeated_char(""), 'None')

    def test_edge_case6(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case7(self):
        self.assertEqual(first_repeated_char("aabbcc"), 'a')

    def test_edge_case8(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case9(self):
        self.assertEqual(first_repeated_char("abc"), 'None')

    def test_edge_case10(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case11(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case12(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case13(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case14(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case15(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case16(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case17(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case18(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case19(self):
        self.assertEqual(first_repeated_char("a"), 'a')

    def test_edge_case20(self):
        self.assertEqual(first_repeated_char("a"), 'a')
