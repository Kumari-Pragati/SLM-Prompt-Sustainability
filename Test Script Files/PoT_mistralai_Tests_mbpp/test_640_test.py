import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_parenthesis(["a(bc)", "def(ghi)", "(jkl)mno"]), ["a bc", "def ghi", "jklmno"])

    def test_empty_string(self):
        self.assertEqual(remove_parenthesis([""]), [""])

    def test_single_char_string(self):
        self.assertEqual(remove_parenthesis(["a"]), ["a"])

    def test_no_parenthesis(self):
        self.assertEqual(remove_parenthesis(["abc", "def", "(ghi)"]), ["abc", "def", "ghi"])

    def test_empty_list(self):
        self.assertEqual(remove_parenthesis([]), [])

    def test_multiple_nested_parenthesis(self):
        self.assertEqual(remove_parenthesis(["(a(bc))", "(def(ghi))"]), ["a bc", "def ghi"])

    def test_parenthesis_with_spaces(self):
        self.assertEqual(remove_parenthesis(["a (bc)", "def (ghi)"]), ["a bc", "def ghi"])

    def test_parenthesis_with_special_characters(self):
        self.assertEqual(remove_parenthesis(["a(1bc)", "def(ghi@)"]), ["a1bc", "def ghi@"])
