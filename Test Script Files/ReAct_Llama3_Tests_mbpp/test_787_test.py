import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_three('abc'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match_three('abababxyz'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match_three('xyzababab'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match_three('ababababab'), 'Found a match!')

    def test_match_found_with_non_matching_text(self):
        self.assertEqual(text_match_three('abcd'), 'Not matched!')

    def test_match_found_with_empty_text(self):
        self.assertEqual(text_match_three(''), 'Not matched!')
