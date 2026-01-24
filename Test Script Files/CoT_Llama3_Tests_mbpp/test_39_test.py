import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(rearange_string("a"), "a")

    def test_two_character_string(self):
        self.assertEqual(rearange_string("ab"), "ab")

    def test_three_character_string(self):
        self.assertEqual(rearange_string("abc"), "abc")

    def test_four_character_string(self):
        self.assertEqual(rearange_string("abcd"), "abcd")

    def test_five_character_string(self):
        self.assertEqual(rearange_string("abcde"), "abcde")

    def test_string_with_repeated_characters(self):
        self.assertEqual(rearange_string("aabbcc"), "aabbc")

    def test_string_with_repeated_characters_and_spaces(self):
        self.assertEqual(rearange_string("aabbcc  "), "aabbc")

    def test_string_with_repeated_characters_and_spaces_and_punctuation(self):
        self.assertEqual(rearange_string("aabbcc."), "aabbc.")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers(self):
        self.assertEqual(rearange_string("aabbcc.123"), "aabbc.123")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters(self):
        self.assertEqual(rearange_string("aabbcc.123!@#"), "aabbc.123!@#")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n"), "aabbc.123!@#\n")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t"), "aabbc.123!@#\n\t")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t\r"), "aabbc.123!@#\n\t\r")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return_and_backslash(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t\r\\"), "aabbc.123!@#\n\t\r\\")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return_and_backslash_and_colon(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t\r\\:"), "aabbc.123!@#\n\t\r:\\\")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t\r\\:,"), "aabbc.123!@#\n\t\r:\\,,")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma_and_semicolon(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t\r\\:,;"), "aabbc.123!@#\n\t\r:\\,;")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma_and_semicolon_and_question_mark(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t\r\\:,;?"), "aabbc.123!@#\n\t\r:\\,;?")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma_and_semicolon_and_question_mark_and_pipe(self):
        self.assertEqual(rearange_string("aabbcc.123!@# \n\t\r\\:,;?|"), "aabbc.123!@#\n\t\r:\\,;?|")

    def test_string_with_repeated_characters_and_spaces_and_punctuation_and_numbers_and_special_characters_and_newline_and_tab_and_carriage_return_and_backslash_and_colon_and_comma_and_semicolon_and_question_mark_and_pipe_and_ampersand(self):
        self.assertEqual(rearange_string("aabbcc.123!@