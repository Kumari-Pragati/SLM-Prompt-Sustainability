import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_char_long("Hello World, this is a test string"), ["World", "test"])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_char_long(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_char_long("Hello"), [])

    def test_edge_case_single_word_with_spaces(self):
        self.assertEqual(find_char_long("Hello World"), [])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_char_long("Hello World, this is a test string"), ["World", "test"])

    def test_edge_case_multiple_words_with_spaces(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with spaces"), ["World", "test"])

    def test_edge_case_multiple_words_with_punctuation(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with spaces and punctuation!"), ["World", "test"])

    def test_edge_case_multiple_words_with_punctuation_and_numbers(self):
        self.assertEqual(find_char_long("Hello World, this is a test string with spaces and punctuation!123"), ["World", "test"])
