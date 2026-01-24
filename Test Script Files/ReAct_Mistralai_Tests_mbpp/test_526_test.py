import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters("word"), "Word")

    def test_multiple_words(self):
        self.assertEqual(capitalize_first_last_letters("first word second word"), "First Word Second word")

    def test_multiple_words_with_numbers(self):
        self.assertEqual(capitalize_first_last_letters("first 123 word second word"), "First 123 Word Second word")

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("first, word. second word!"), "First, Word. Second word!")

    def test_single_word_with_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("word."), "Word.")

    def test_single_word_with_numbers_and_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("123word."), "123Word.")

    def test_all_uppercase(self):
        self.assertEqual(capitalize_first_last_letters("WORD"), "Word")

    def test_all_lowercase(self):
        self.assertEqual(capitalize_first_last_letters("word"), "Word")

    def test_all_capitalized(self):
        self.assertEqual(capitalize_first_last_letters("Word"), "Word")

    def test_long_string(self):
        long_string = "a" * 100
        self.assertEqual(capitalize_first_last_letters(long_string), long_string[:1] + long_string[1:-1].title() + long_string[-1].upper())
