import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_found_match_with_z(self):
        self.assertEqual(text_match_wordz('wordz'), 'Found a match!')

    def test_found_match_with_z_at_beginning(self):
        self.assertEqual(text_match_wordz('zword'), 'Found a match!')

    def test_found_match_with_z_at_end(self):
        self.assertEqual(text_match_wordz('wordzx'), 'Found a match!')

    def test_found_match_with_z_in_middle(self):
        self.assertEqual(text_match_wordz('wordzword'), 'Found a match!')

    def test_not_found_match_without_z(self):
        self.assertEqual(text_match_wordz('word'), 'Not matched!')

    def test_not_found_match_with_z_replaced(self):
        self.assertEqual(text_match_wordz('wordzx'), 'Not matched!')

    def test_not_found_match_with_z_at_beginning_and_end(self):
        self.assertEqual(text_match_wordz('zwordz'), 'Not matched!')
