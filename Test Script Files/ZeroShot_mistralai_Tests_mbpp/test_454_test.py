import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_match_with_z(self):
        self.assertEqual(text_match_wordz('Hello worldz'), 'Found a match!')

    def test_match_without_z(self):
        self.assertEqual(text_match_wordz('Hello world'), 'Not matched!')

    def test_match_at_beginning(self):
        self.assertEqual(text_match_wordz('zHello world'), 'Found a match!')

    def test_match_at_end(self):
        self.assertEqual(text_match_wordz('Hello worldz'), 'Found a match!')

    def test_match_in_middle(self):
        self.assertEqual(text_match_wordz('Hello zWorld'), 'Found a match!')

    def test_match_with_multiple_zs(self):
        self.assertEqual(text_match_wordz('Hello zZWorld'), 'Found a match!')

    def test_match_with_numbers(self):
        self.assertEqual(text_match_wordz('Hello123zWorld'), 'Found a match!')

    def test_match_with_special_characters(self):
        self.assertEqual(text_match_wordz('Hello#zWorld'), 'Found a match!')
