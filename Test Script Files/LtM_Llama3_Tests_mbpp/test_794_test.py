import unittest
from mbpp_794_code import text_starta_endb

class TestTextStartaEndb(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_starta_endb("aabb"), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_starta_endb("abc"), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_starta_endb(""), 'Not matched!')

    def test_pattern_at_start(self):
        self.assertEqual(text_starta_endb("aabbcc"), 'Found a match!')

    def test_pattern_at_end(self):
        self.assertEqual(text_starta_endb("abbaabb"), 'Found a match!')

    def test_pattern_in_middle(self):
        self.assertEqual(text_starta_endb("abbaabbcc"), 'Found a match!')

    def test_pattern_at_start_and_end(self):
        self.assertEqual(text_starta_endb("aabbcc"), 'Found a match!')

    def test_pattern_at_start_and_middle(self):
        self.assertEqual(text_starta_endb("aabbabba"), 'Found a match!')

    def test_pattern_at_end_and_middle(self):
        self.assertEqual(text_starta_endb("abbaabba"), 'Found a match!')

    def test_pattern_at_start_and_end_and_middle(self):
        self.assertEqual(text_starta_endb("aabbabbaabb"), 'Found a match!')
