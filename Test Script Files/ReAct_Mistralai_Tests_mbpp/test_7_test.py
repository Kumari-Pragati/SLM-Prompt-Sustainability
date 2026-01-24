import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(find_char_long(""), [])

    def test_single_word(self):
        self.assertListEqual(find_char_long("word"), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(find_char_long("LongWordShortWord"), ["LongWord", "ShortWord"])

    def test_long_words(self):
        self.assertListEqual(find_char_long("ThisIsALongWordThatIsLongerThanFourCharacters"), ["ThisIsALongWordThatIsLongerThanFourCharacters"])

    def test_words_with_four_characters(self):
        self.assertListEqual(find_char_long("Word1Word2Word3Word4"), ["Word1", "Word2", "Word3", "Word4"])

    def test_words_with_exactly_four_characters(self):
        self.assertListEqual(find_char_long("Word1234"), ["Word1234"])

    def test_words_with_leading_and_trailing_spaces(self):
        self.assertListEqual(find_char_long(" Word123 Word456 "), ["Word123", "Word456"])

    def test_words_with_only_numbers(self):
        self.assertListEqual(find_char_long("12345678"), [])

    def test_words_with_only_special_characters(self):
        self.assertListEqual(find_char_long("!@#$%^&*()"), [])

    def test_words_with_mixed_characters(self):
        self.assertListEqual(find_char_long("Word1!@#$%^&*()"), ["Word1"])

    def test_words_with_punctuation_at_beginning_and_end(self):
        self.assertListEqual(find_char_long(".,;:!?@#$%^&*()[]{}<>\"'\\|_`~-+=[]{}"), [])

    def test_words_with_punctuation_in_middle(self):
        self.assertListEqual(find_char_long("Word.,;:!?@#$%^&*()[]{}<>\"'\\|_`~-+=[]{}Word"), ["Word"])
