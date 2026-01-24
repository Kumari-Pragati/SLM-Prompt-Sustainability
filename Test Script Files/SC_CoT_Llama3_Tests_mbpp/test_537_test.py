import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(first_repeated_word("hello world hello"), "hello")

    def test_edge_case_empty_string(self):
        self.assertEqual(first_repeated_word(""), 'None')

    def test_edge_case_single_word(self):
        self.assertEqual(first_repeated_word("hello"), 'None')

    def test_edge_case_single_word_repeated(self):
        self.assertEqual(first_repeated_word("hello hello"), "hello")

    def test_edge_case_multiple_words_no_repeats(self):
        self.assertEqual(first_repeated_word("hello world"), 'None')

    def test_edge_case_multiple_words_with_repeats(self):
        self.assertEqual(first_repeated_word("hello world hello world"), "hello")

    def test_edge_case_multiple_words_with_repeats_and_duplicates(self):
        self.assertEqual(first_repeated_word("hello world hello world hello"), "hello")

    def test_edge_case_multiple_words_with_repeats_and_duplicates_and_empty(self):
        self.assertEqual(first_repeated_word("hello world hello world hello"), "hello")

    def test_edge_case_empty_string_and_single_word(self):
        self.assertEqual(first_repeated_word("hello"), 'None')

    def test_edge_case_empty_string_and_multiple_words(self):
        self.assertEqual(first_repeated_word("hello world"), 'None')

    def test_edge_case_empty_string_and_multiple_words_with_repeats(self):
        self.assertEqual(first_repeated_word("hello world hello world"), "hello")

    def test_edge_case_empty_string_and_multiple_words_with_repeats_and_duplicates(self):
        self.assertEqual(first_repeated_word("hello world hello world hello"), "hello")

    def test_edge_case_empty_string_and_multiple_words_with_repeats_and_duplicates_and_empty(self):
        self.assertEqual(first_repeated_word("hello world hello world hello"), "hello")
