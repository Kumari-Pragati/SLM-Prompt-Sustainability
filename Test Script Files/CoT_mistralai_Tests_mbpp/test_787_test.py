import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_match_three_letters(self):
        self.assertEqual(text_match_three('abc'), 'Found a match!')

    def test_match_three_letters_with_space(self):
        self.assertEqual(text_match_three('abc def'), 'Not matched!')

    def test_match_three_letters_with_repetition(self):
        self.assertEqual(text_match_three('aaabbbccc'), 'Found a match!')

    def test_match_three_letters_with_question_mark(self):
        self.assertEqual(text_match_three('abc?c'), 'Found a match!')

    def test_match_three_letters_with_different_case(self):
        self.assertEqual(text_match_three('ABC'), 'Found a match!')

    def test_match_three_letters_with_empty_string(self):
        self.assertEqual(text_match_three(''), 'Not matched!')

    def test_match_three_letters_with_single_letter(self):
        self.assertEqual(text_match_three('a'), 'Not matched!')

    def test_match_three_letters_with_two_letters(self):
        self.assertEqual(text_match_three('ab'), 'Not matched!')
