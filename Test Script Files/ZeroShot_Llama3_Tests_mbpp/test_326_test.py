import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(most_occurrences([]), '')

    def test_single_word(self):
        self.assertEqual(most_occurrences(['hello']), 'hello')

    def test_multiple_words(self):
        self.assertEqual(most_occurrences(['hello', 'world', 'hello']), 'hello')

    def test_multiple_words_with_duplicates(self):
        self.assertEqual(most_occurrences(['hello', 'world', 'hello', 'hello']), 'hello')

    def test_multiple_words_with_duplicates_and_spaces(self):
        self.assertEqual(most_occurrences(['hello', 'world', 'hello hello']), 'hello')

    def test_multiple_words_with_duplicates_and_spaces_and_punctuation(self):
        self.assertEqual(most_occurrences(['hello', 'world', 'hello hello, world!']), 'hello')

    def test_multiple_words_with_duplicates_and_spaces_and_punctuation_and_numbers(self):
        self.assertEqual(most_occurrences(['hello', 'world', 'hello hello, world! 123']), 'hello')

    def test_multiple_words_with_duplicates_and_spaces_and_punctuation_and_numbers_and_special_chars(self):
        self.assertEqual(most_occurrences(['hello', 'world', 'hello hello, world! 123 @#']), 'hello')
