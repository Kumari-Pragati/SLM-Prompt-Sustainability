import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_single_word(self):
        self.assertEqual(find_Max_Len_Even("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(find_Max_Len_Even("hello world"), "hello")

    def test_multiple_words_with_spaces(self):
        self.assertEqual(find_Max_Len_Even("hello  world"), "hello")

    def test_multiple_words_with_spaces_and_newline(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\""), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\"'"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe_and_dollar(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\"'$$"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe_and_dollar_and_percent(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\"'$$%"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe_and_dollar_and_percent_and_ampersand(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\"'$$%&"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe_and_dollar_and_percent_and_ampersand_and_parenthesis(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\"'$$%&(())"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe_and_dollar_and_percent_and_ampersand_and_parenthesis_and_brackets(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\"'$$%&(())[]"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe_and_dollar_and_percent_and_ampersand_and_parenthesis_and_brackets_and_angle_brackets(self):
        self.assertEqual(find_Max_Len_Even("hello\nworld\t\r:,;\\"\"'$$%&(())[]<>"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_backslash_and_quote_and_apostrophe_and_dollar_and_percent_and_ampersand_and_parenthesis_and_brackets_and_angle_br