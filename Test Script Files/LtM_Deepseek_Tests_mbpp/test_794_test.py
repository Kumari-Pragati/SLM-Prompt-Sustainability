import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_starta_endb('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_starta_endb('ac'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_match_with_spaces(self):
        self.assertEqual(text_starta_endb('a b'), 'Found a match!')

    def test_match_with_special_characters(self):
        self.assertEqual(text_starta_endb('a@#$b'), 'Found a match!')

    def test_match_with_numbers(self):
        self.assertEqual(text_starta_endb('a123b'), 'Found a match!')

    def test_no_a(self):
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_no_b(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb('aabbb'), 'Not matched!')
