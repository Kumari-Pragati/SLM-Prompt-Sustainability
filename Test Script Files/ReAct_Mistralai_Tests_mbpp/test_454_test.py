import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):

    def test_match_with_z_at_end(self):
        self.assertEqual(text_match_wordz("Hello worldz"), 'Found a match!')

    def test_match_with_z_in_middle(self):
        self.assertEqual(text_match_wordz("Hello worldz123"), 'Found a match!')

    def test_match_with_z_at_beginning(self):
        self.assertEqual(text_match_wordz("zHello world"), 'Found a match!')

    def test_match_with_multiple_zs(self):
        self.assertEqual(text_match_wordz("Hello worldzzz"), 'Found a match!')

    def test_no_match_no_z(self):
        self.assertEqual(text_match_wordz("Hello world"), 'Not matched!')

    def test_no_match_no_word(self):
        self.assertEqual(text_match_wordz("123"), 'Not matched!')

    def test_no_match_z_not_at_end(self):
        self.assertEqual(text_match_wordz("Hello worldz123"), 'Not matched!')
