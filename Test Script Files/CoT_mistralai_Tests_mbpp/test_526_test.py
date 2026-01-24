import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_single_word(self):
        self.assertEqual(capitalize_first_last_letters("word"), "Word")

    def test_multiple_words(self):
        self.assertEqual(capitalize_first_last_letters("first second third"), "First Second Third")

    def test_mixed_case_single_word(self):
        self.assertEqual(capitalize_first_last_letters("Word"), "Word")

    def test_mixed_case_multiple_words(self):
        self.assertEqual(capitalize_first_last_letters("First Word Second Word"), "First Word Second word")

    def test_punctuation_at_beginning(self):
        self.assertEqual(capitalize_first_last_letters(".,!@#$%^&*()_First Word Second Word"), ".!@#$%^&*()_First Word second word")

    def test_punctuation_at_end(self):
        self.assertEqual(capitalize_first_last_letters("First Word Second Word."), "First Word second word.")

    def test_punctuation_in_middle(self):
        self.assertEqual(capitalize_first_last_letters("First Word, Second Word."), "First Word, second word.")

    def test_multiple_spaces(self):
        self.assertEqual(capitalize_first_last_letters("First   Word   Second   Word"), "First Word Second word")

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(capitalize_first_last_letters("   First Word   Second Word   "), "First Word Second word")

    def test_empty_word(self):
        self.assertEqual(capitalize_first_last_letters(""), "")

    def test_single_empty_word(self):
        self.assertEqual(capitalize_first_last_letters("   "), "")

    def test_multiple_empty_words(self):
        self.assertEqual(capitalize_first_last_letters("   First   Second   "), "First Second")
