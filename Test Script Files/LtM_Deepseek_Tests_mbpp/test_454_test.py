import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_wordz('examplez'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_wordz('example'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match_wordz('ex@mplez'), 'Found a match!')

    def test_numbers_in_word(self):
        self.assertEqual(text_match_wordz('exampl3z'), 'Found a match!')

    def test_multiple_words(self):
        self.assertEqual(text_match_wordz('examplez anotherz'), 'Found a match!')

    def test_word_without_z(self):
        self.assertEqual(text_match_wordz('example'), 'Not matched!')

    def test_word_with_z_at_end(self):
        self.assertEqual(text_match_wordz('examplez'), 'Found a match!')

    def test_word_with_z_at_start(self):
        self.assertEqual(text_match_wordz('zexample'), 'Found a match!')
