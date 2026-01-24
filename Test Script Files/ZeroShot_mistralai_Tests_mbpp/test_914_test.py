import unittest
from914_code import is_Two_Alter

class TestIsTwoAlter(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_Two_Alter(""))

    def test_single_character(self):
        self.assertTrue(is_Two_Alter("a"))
        self.assertTrue(is_Two_Alter("b"))
        self.assertTrue(is_Two_Alter("c"))

    def test_two_characters(self):
        self.assertFalse(is_Two_Alter("aa"))
        self.assertFalse(is_Two_Alter("ab"))
        self.assertTrue(is_Two_Alter("ac"))
        self.assertTrue(is_Two_Alter("ba"))
        self.assertTrue(is_Two_Alter("bc"))

    def test_three_characters(self):
        self.assertFalse(is_Two_Alter("aaa"))
        self.assertTrue(is_Two_Alter("aab"))
        self.assertTrue(is_Two_Alter("aac"))
        self.assertTrue(is_Two_Alter("aba"))
        self.assertTrue(is_Two_Alter("abc"))

    def test_four_characters(self):
        self.assertFalse(is_Two_Alter("aaaa"))
        self.assertTrue(is_Two_Alter("aaab"))
        self.assertTrue(is_Two_Alter("aaac"))
        self.assertTrue(is_Two_Alter("aaba"))
        self.assertTrue(is_Two_Alter("aabc"))
        self.assertTrue(is_Two_Alter("abab"))
        self.assertTrue(is_Two_Alter("abac"))
        self.assertTrue(is_Two_Alter("abcab"))
        self.assertTrue(is_Two_Alter("abcac"))

    def test_five_characters(self):
        self.assertFalse(is_Two_Alter("aaaaa"))
        self.assertTrue(is_Two_Alter("aaaaa"))
        self.assertTrue(is_Two_Alter("aaaab"))
        self.assertTrue(is_Two_Alter("aaaac"))
        self.assertTrue(is_Two_Alter("aaaba"))
        self.assertTrue(is_Two_Alter("aaabc"))
        self.assertTrue(is_Two_Alter("aabab"))
        self.assertTrue(is_Two_Alter("aabac"))
        self.assertTrue(is_Two_Alter("ababab"))
        self.assertTrue(is_Two_Alter("ababac"))
        self.assertTrue(is_Two_Alter("abacab"))
        self.assertTrue(is_Two_Alter("abcabc"))
        self.assertTrue(is_Two_Alter("abcacb"))
        self.assertTrue(is_Two_Alter("abcac"))
