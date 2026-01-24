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

    def test_punctuation(self):
        self.assertEqual(capitalize_first_last_letters("Hello, World!"), "Hello, world!")

    def test_special_characters(self):
        self.assertEqual(capitalize_first_last_letters("123_AbCd_EfGh_IjKl_MnOp"), "123 AbCd EfGh IjKl MnOp")
