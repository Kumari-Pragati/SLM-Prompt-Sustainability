import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_long_words(self):
        self.assertListEqual(find_char_long("This is a test string"), ["test", "string"])

    def test_single_word(self):
        self.assertListEqual(find_char_long("word"), ["word"])

    def test_empty_string(self):
        self.assertListEqual(find_char_long(""), [])

    def test_short_words(self):
        self.assertListEqual(find_char_long("abc"), [])

    def test_multi_word_with_short_words(self):
        self.assertListEqual(find_char_long("short word long word"), ["long", "word"])

    def test_punctuation(self):
        self.assertListEqual(find_char_long("This,is!a?test!string"), [])

    def test_numbers(self):
        self.assertListEqual(find_char_long("1234test5678"), [])
