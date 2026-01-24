import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_single_a_and_b(self):
        self.assertEqual(text_starta_endb('ab'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb('aaabbb'), 'Not matched!')

    def test_match_a_at_start_and_b_at_end(self):
        self.assertEqual(text_starta_endb('aab'), 'Not matched!')

    def test_match_a_at_start_and_b_anywhere(self):
        self.assertEqual(text_starta_endb('aabb'), 'Not matched!')

    def test_match_a_anywhere_and_b_at_end(self):
        self.assertEqual(text_starta_endb('baab'), 'Not matched!')

    def test_match_a_at_start_and_b_at_end(self):
        self.assertEqual(text_starta_endb('aab'), 'Found a match!')

    def test_match_multiple_a_at_start_and_b_at_end(self):
        self.assertEqual(text_starta_endb('aaaaabbb'), 'Found a match!')
