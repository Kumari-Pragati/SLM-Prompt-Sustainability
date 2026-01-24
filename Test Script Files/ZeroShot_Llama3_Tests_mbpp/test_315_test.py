import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_single_word(self):
        self.assertEqual(find_Max_Len_Even("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(find_Max_Len_Even("hello world"), "world")

    def test_multiple_words_with_spaces(self):
        self.assertEqual(find_Max_Len_Even("   hello   world   "), "world")

    def test_multiple_words_with_spaces_and_punctuation(self):
        self.assertEqual(find_Max_Len_Even("   hello, world!   "), "world")

    def test_multiple_words_with_spaces_and_punctuation_and_numbers(self):
        self.assertEqual(find_Max_Len_Even("   hello, world! 123   "), "world")

    def test_multiple_words_with_spaces_and_punctuation_and_numbers_and_special_characters(self):
        self.assertEqual(find_Max_Len_Even("   hello, world! 123 @#   "), "world")

    def test_multiple_words_with_spaces_and_punctuation_and_numbers_and_special_characters_and_newlines(self):
        self.assertEqual(find_Max_Len_Even("   hello,\r\nworld! 123 @#   "), "world")

    def test_multiple_words_with_spaces_and_punctuation_and_numbers_and_special_characters_and_newlines_and_tabs(self):
        self.assertEqual(find_Max_Len_Even("   hello,\r\nworld! 123 @#   \t"), "world")

    def test_multiple_words_with_spaces_and_punctuation_and_numbers_and_special_characters_and_newlines_and_tabs_and_carriage_return(self):
        self.assertEqual(find_Max_Len_Even("   hello,\r\nworld! 123 @#   \t\r"), "world")

    def test_multiple_words_with_spaces_and_punctuation_and_numbers_and_special_characters_and_newlines_and_tabs_and_carriage_return_and_backslash(self):
        self.assertEqual(find_Max_Len_Even("   hello,\r\nworld! 123 @#   \t\r\\"), "world")
