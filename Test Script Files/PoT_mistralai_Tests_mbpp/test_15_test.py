import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(split_lowerstring("HelloWorld"), ["hello", "world"])
        self.assertListEqual(split_lowerstring("PythonProgramming"), ["python", "programming"])
        self.assertListEqual(split_lowerstring("JavaScriptIsFun"), ["javascript", "is", "fun"])

    def test_edge_case_empty_string(self):
        self.assertListEqual(split_lowerstring(""), [])

    def test_edge_case_single_word(self):
        self.assertListEqual(split_lowerstring("word"), ["word"])

    def test_edge_case_single_letter(self):
        self.assertListEqual(split_lowerstring("a"), ["a"])

    def test_edge_case_all_uppercase(self):
        self.assertListEqual(split_lowerstring("HELLO"), ["hello"])

    def test_edge_case_all_digits(self):
        self.assertListEqual(split_lowerstring("123456"), [])

    def test_edge_case_special_characters(self):
        self.assertListEqual(split_lowerstring("!@#$%^&*()_+-=[]{};':\"\\|,.<>/?"), [])

    def test_edge_case_mixed_case(self):
        self.assertListEqual(split_lowerstring("HeLloWoRlD"), ["hello", "world"])
