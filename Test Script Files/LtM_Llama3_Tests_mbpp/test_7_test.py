import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(find_char_long(""), [])

    def test_single_word(self):
        self.assertEqual(find_char_long("hello"), [])

    def test_multiple_words(self):
        self.assertEqual(find_char_long("hello world"), [])

    def test_word_with_four_characters(self):
        self.assertEqual(find_char_long("helloabc"), ["abc"])

    def test_word_with_five_characters(self):
        self.assertEqual(find_char_long("helloabcd"), ["abcd"])

    def test_word_with_six_characters(self):
        self.assertEqual(find_char_long("helloabcdef"), ["abcdef"])

    def test_word_with_seven_characters(self):
        self.assertEqual(find_char_long("helloabcdefg"), ["abcdefg"])

    def test_word_with_eight_characters(self):
        self.assertEqual(find_char_long("helloabcdefgh"), ["abcdefgh"])

    def test_multiple_words_with_four_characters(self):
        self.assertEqual(find_char_long("abcde abfgh"), ["abcde", "abfgh"])

    def test_multiple_words_with_five_characters(self):
        self.assertEqual(find_char_long("abcde abfghi"), ["abcde", "abfghi"])

    def test_multiple_words_with_six_characters(self):
        self.assertEqual(find_char_long("abcde abfghij"), ["abcde", "abfghij"])

    def test_multiple_words_with_seven_characters(self):
        self.assertEqual(find_char_long("abcde abfghijk"), ["abcde", "abfghijk"])

    def test_multiple_words_with_eight_characters(self):
        self.assertEqual(find_char_long("abcde abfghijkl"), ["abcde", "abfghijkl"])
