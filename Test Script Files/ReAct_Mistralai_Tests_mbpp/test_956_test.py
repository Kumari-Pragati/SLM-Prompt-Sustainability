import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(split_list(""), [])

    def test_single_uppercase_letter(self):
        self.assertListEqual(split_list("A"), ["A"])

    def test_multiple_uppercase_letters(self):
        self.assertListEqual(split_list("ABC"), ["AB", "C"])

    def test_mixed_case_letters(self):
        self.assertListEqual(split_list("aBc"), ["aB", "c"])

    def test_multiple_words(self):
        self.assertListEqual(split_list("Hello World"), ["Hello", "World"])

    def test_leading_punctuation(self):
        self.assertListEqual(split_list(".,!?Hello World"), ["Hello", "World"])

    def test_trailing_punctuation(self):
        self.assertListEqual(split_list("Hello World."), ["Hello", "World"])

    def test_multiple_punctuation(self):
        self.assertListEqual(split_list(".,!?Hello World!?"), ["Hello", "World"])

    def test_empty_word(self):
        self.assertListEqual(split_list(" A "), ["A"])

    def test_whitespace_only(self):
        self.assertListEqual(split_list("   "), [])

    def test_non_alphabetic_characters(self):
        self.assertListEqual(split_list("123ABC456"), ["123", "ABC", "456"])

    def test_multiple_non_alphabetic_characters(self):
        self.assertListEqual(split_list("123ABC456!@#"), ["123", "ABC", "456"])
