import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6"), ["World", "test", "words", "length", "string"])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_char_long(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_char_long("Hello"), [])

    def test_edge_case_single_word_with_length_4(self):
        self.assertEqual(find_char_long("abcd"), ["abcd"])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7"), ["World", "test", "words", "length", "string"])

    def test_edge_case_multiple_words_with_length_4(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7, and 4"), ["World", "test", "words", "length", "string", "and"])

    def test_edge_case_multiple_words_with_length_4_and_5(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7, and 5"), ["World", "test", "words", "length", "string", "and"])

    def test_edge_case_multiple_words_with_length_4_and_6(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7, and 6"), ["World", "test", "words", "length", "string", "and"])

    def test_edge_case_multiple_words_with_length_4_and_7(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7, and 7"), ["World", "test", "words", "length", "string", "and"])

    def test_edge_case_multiple_words_with_length_4_and_8(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7, and 8"), ["World", "test", "words", "length", "string", "and"])

    def test_edge_case_multiple_words_with_length_4_and_9(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7, and 9"), ["World", "test", "words", "length", "string", "and"])

    def test_edge_case_multiple_words_with_length_4_and_10(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with words of length 4, 5, 6, and 7, and 10"), ["World", "test", "words", "length", "string", "and"])
