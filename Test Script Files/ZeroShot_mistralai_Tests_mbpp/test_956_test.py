import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(split_list(""), [])

    def test_single_word(self):
        self.assertEqual(split_list("Word"), ["Word"])

    def test_multiple_words(self):
        self.assertEqual(split_list("First Word Second Word"), ["First", "Word", "Second"])

    def test_mixed_case_words(self):
        self.assertEqual(split_list("First Word Second Word"), ["First", "Word", "Second"])

    def test_punctuation(self):
        self.assertEqual(split_list("First Word, Second Word!"), ["First", "Word", "Second"])

    def test_numbers(self):
        self.assertEqual(split_list("First 123 Word Second Word"), ["First", "123", "Word", "Second"])

    def test_special_characters(self):
        self.assertEqual(split_list("First@Word Second#Word"), ["First", "Word", "Second"])

    def test_multiple_spaces(self):
        self.assertEqual(split_list(" First Word   Second Word  "), ["First", "Word", "Second"])
