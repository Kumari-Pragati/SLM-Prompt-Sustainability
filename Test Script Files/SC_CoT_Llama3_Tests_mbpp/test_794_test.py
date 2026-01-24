import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_starta_endb("aabb"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_starta_endb("abc"), 'Not matched!')

    def test_match_at_start(self):
        self.assertEqual(text_starta_endb("aabbcc"), 'Found a match!')

    def test_match_at_end(self):
        self.assertEqual(text_starta_endb("abcba"), 'Found a match!')

    def test_match_in_middle(self):
        self.assertEqual(text_starta_endb("ababba"), 'Found a match!')

    def test_no_match_at_start(self):
        self.assertEqual(text_starta_endb("babc"), 'Not matched!')

    def test_no_match_at_end(self):
        self.assertEqual(text_starta_endb("abcba"), 'Not matched!')

    def test_no_match_in_middle(self):
        self.assertEqual(text_starta_endb("abccba"), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_starta_endb(""), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_starta_endb(123)
