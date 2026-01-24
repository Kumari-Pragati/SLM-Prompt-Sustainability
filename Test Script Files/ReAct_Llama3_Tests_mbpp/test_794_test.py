import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_starta_endb("aabb"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_starta_endb("abc"), 'Not matched!')

    def test_found_match_at_start(self):
        self.assertEqual(text_starta_endb("aabbcc"), 'Found a match!')

    def test_found_match_at_end(self):
        self.assertEqual(text_starta_endb("abbaabb"), 'Found a match!')

    def test_found_match_at_start_and_end(self):
        self.assertEqual(text_starta_endb("aabbbaabb"), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_starta_endb(""), 'Not matched!')

    def test_no_match(self):
        self.assertEqual(text_starta_endb("abcde"), 'Not matched!')
