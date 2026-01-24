import unittest
from mbpp_128_code import long_words

class TestLongWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(long_words(1, ""), [])

    def test_single_word(self):
        self.assertListEqual(long_words(1, "one"), ["one"])
        self.assertListEqual(long_words(2, "one"), ["one"])
        self.assertListEqual(long_words(3, "one"), ["one"])

    def test_multiple_words(self):
        self.assertListEqual(long_words(2, "one two three four"), ["three", "four"])
        self.assertListEqual(long_words(3, "one two three four"), ["three", "four"])
        self.assertListEqual(long_words(4, "one two three four"), ["three", "four"])

    def test_long_words(self):
        self.assertListEqual(long_words(3, "elephant ant aardvark"), ["elephant", "aardvark"])

    def test_short_words(self):
        self.assertListEqual(long_words(4, "apple banana cherry"), [])

    def test_single_long_word(self):
        self.assertListEqual(long_words(5, "elephants"), ["elephants"])

    def test_punctuation(self):
        self.assertListEqual(long_words(3, "Hello, World!"), [])

    def test_empty_list(self):
        self.assertListEqual(long_words(3, ""), [])

    def test_whitespace_only(self):
        self.assertListEqual(long_words(3, "   "), [])
