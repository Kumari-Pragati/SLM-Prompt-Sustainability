import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(find_char(""), [])

    def test_single_word(self):
        self.assertListEqual(find_char("word"), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(find_char("This is a test"), ["This", "is", "a", "test"])

    def test_long_word(self):
        self.assertListEqual(find_char("Thisisatestwithalongword"), ["Thisisatest", "long", "word"])

    def test_short_word(self):
        self.assertListEqual(find_char("Thisisatest"), ["This", "is", "atest"])

    def test_word_with_numbers(self):
        self.assertListEqual(find_char("This123isatest"), ["This", "is", "atest"])

    def test_word_with_special_characters(self):
        self.assertListEqual(find_char("This#$%^&*isatest"), ["This", "is", "atest"])

    def test_word_with_punctuation(self):
        self.assertListEqual(find_char("This,is,a,test."), ["This", "is", "a", "test"])

    def test_word_with_whitespace_only(self):
        self.assertListEqual(find_char("   "), [])

    def test_word_with_only_numbers(self):
        self.assertListEqual(find_char("12345"), [])

    def test_word_with_only_special_characters(self):
        self.assertListEqual(find_char("#$%^&*"), [])

    def test_word_with_only_punctuation(self):
        self.assertListEqual(find_char(".,;:!?"), [])

    def test_word_with_mixed_types(self):
        self.assertListEqual(find_char("This is 123test#$%^&*"), ["This", "is", "123test"])
