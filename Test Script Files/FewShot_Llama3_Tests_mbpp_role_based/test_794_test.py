import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_starta_endb('aabb'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_starta_endb('hello'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_starta_endb('aabbcc'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_starta_endb('abcba'), 'Found a match!')

    def test_match_found_at_middle(self):
        self.assertEqual(text_starta_endb('abcbab'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(''), 'Not matched!')

    def test_no_match(self):
        self.assertEqual(text_starta_endb('hello world'), 'Not matched!')
