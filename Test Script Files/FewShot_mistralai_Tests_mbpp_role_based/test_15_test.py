import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertListEqual(split_lowerstring("HelloWorld"), ["hello", "world"])

    def test_empty_string(self):
        self.assertListEqual(split_lowerstring(""), [])

    def test_single_word(self):
        self.assertListEqual(split_lowerstring("word"), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(split_lowerstring("ThisIsATest"), ["this", "is", "a", "test"])

    def test_mixed_case_string(self):
        self.assertListEqual(split_lowerstring("HeLlO wOrLd"), ["hello", "world"])

    def test_string_with_numbers(self):
        self.assertListEqual(split_lowerstring("123Hello456World789"), ["hello", "world"])

    def test_string_with_special_characters(self):
        self.assertListEqual(split_lowerstring("Hello@World#"), ["hello", "world"])
