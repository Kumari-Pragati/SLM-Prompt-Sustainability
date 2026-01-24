import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_starta_endb("aabb"), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_starta_endb("abc"), 'Not matched!')

    def test_match_at_start(self):
        self.assertEqual(text_starta_endb("aabbcc"), 'Found a match!')

    def test_match_at_end(self):
        self.assertEqual(text_starta_endb("abcba"), 'Found a match!')

    def test_match_at_start_and_end(self):
        self.assertEqual(text_starta_endb("aabbba"), 'Found a match!')

    def test_no_match_at_start(self):
        self.assertEqual(text_starta_endb("abc"), 'Not matched!')

    def test_no_match_at_end(self):
        self.assertEqual(text_starta_endb("abcba"), 'Not matched!')
