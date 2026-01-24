import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_starta_endb('aaab'), 'Found a match!')

    def test_match_with_spaces(self):
        self.assertEqual(text_starta_endb(' aaab '), 'Found a match!')

    def test_match_case_insensitive(self):
        self.assertEqual(text_starta_endb('Aaab'), 'Found a match!')

    def test_match_with_preceding_characters(self):
        self.assertEqual(text_starta_endb('xyz aaab'), 'Found a match!')

    def test_match_with_succeeding_characters(self):
        self.assertEqual(text_starta_endb('aaab pqr'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_no_a(self):
        self.assertEqual(text_starta_endb('bbb'), 'Not matched!')

    def test_no_b(self):
        self.assertEqual(text_starta_endb('aaa'), 'Not matched!')

    def test_only_a(self):
        self.assertEqual(text_starta_endb('aa'), 'Not matched!')

    def test_only_b(self):
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb('aaaaabbbb'), 'Not matched!')
