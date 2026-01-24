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
        self.assertEqual(find_Max_Len_Even("hello  world\n"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t\r"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t\r:"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t\r:,"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t\r:,;"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_question_mark(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t\r:,;?"), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_question_mark_and_period(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t\r:,;?."), "hello")

    def test_multiple_words_with_spaces_and_newline_and_tab_and_carriage_return_and_colon_and_comma_and_semicolon_and_question_mark_and_period_and_exclamation_mark(self):
        self.assertEqual(find_Max_Len_Even("hello  world\n\t\r:,;?.!"), "hello")
