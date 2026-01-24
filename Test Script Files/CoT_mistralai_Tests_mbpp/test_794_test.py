import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):
    def test_found_match(self):
        self.assertEqual(text_starta_endb('aaab'), 'Found a match!')
        self.assertEqual(text_starta_endb('aaaab'), 'Found a match!')
        self.assertEqual(text_starta_endb('aaaabcc'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_starta_endb('a'), 'Not matched!')

    def test_single_b(self):
        self.assertEqual(text_starta_endb('b'), 'Not matched!')

    def test_no_a(self):
        self.assertEqual(text_starta_endb('abc'), 'Not matched!')

    def test_no_b(self):
        self.assertEqual(text_starta_endb('aaa'), 'Not matched!')

    def test_multiple_b(self):
        self.assertEqual(text_starta_endb('aaabbb'), 'Not matched!')

    def test_multiple_a_and_b(self):
        self.assertEqual(text_starta_endb('aaaaabbb'), 'Found a match!')
