import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(length_Of_Last_Word(""), 0)

    def test_single_word(self):
        self.assertEqual(length_Of_Last_Word("hello"), 5)

    def test_multiple_words(self):
        self.assertEqual(length_Of_Last_Word("hello world"), 5)

    def test_multiple_words_with_spaces_before_last(self):
        self.assertEqual(length_Of_Last_Word(" world"), 0)

    def test_multiple_words_with_spaces_after_last(self):
        self.assertEqual(length_Of_Last_Word("hello   "), 5)

    def test_single_word_with_leading_spaces(self):
        self.assertEqual(length_Of_Last_Word("   hello"), 5)

    def test_single_word_with_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("hello   "), 5)

    def test_single_word_with_leading_and_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("   hello   "), 5)

    def test_only_spaces(self):
        self.assertEqual(length_Of_Last_Word("   "), 0)

    def test_non_string_input(self):
        self.assertRaises(TypeError, length_Of_Last_Word, 123)
