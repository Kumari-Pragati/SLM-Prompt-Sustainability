import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_match_three_letters(self):
        self.assertEqual(text_match_three('abc'), 'Found a match!')

    def test_match_three_letters_with_question_mark(self):
        self.assertEqual(text_match_three('aba'), 'Found a match!')

    def test_match_three_letters_with_spaces(self):
        self.assertEqual(text_match_three('abc def'), 'Not matched!')

    def test_match_three_letters_with_different_case(self):
        self.assertEqual(text_match_three('ABC'), 'Not matched!')

    def test_match_three_letters_with_less_than_three(self):
        self.assertEqual(text_match_three('ab'), 'Not matched!')
