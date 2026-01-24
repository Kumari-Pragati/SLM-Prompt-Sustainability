import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_three('abc'), 'Not matched!')

    def test_found_match_at_start(self):
        self.assertEqual(text_match_three('abababc'), 'Found a match!')

    def test_found_match_at_end(self):
        self.assertEqual(text_match_three('abcabab'), 'Found a match!')

    def test_found_match_in_middle(self):
        self.assertEqual(text_match_three('ababababc'), 'Found a match!')

    def test_found_match_multiple_times(self):
        self.assertEqual(text_match_three('ababababab'), 'Found a match!')

    def test_found_match_non_matching(self):
        self.assertEqual(text_match_three('abababababab'), 'Found a match!')

    def test_found_match_non_matching_at_start(self):
        self.assertEqual(text_match_three('abcabababab'), 'Found a match!')

    def test_found_match_non_matching_at_end(self):
        self.assertEqual(text_match_three('abababababc'), 'Found a match!')

    def test_found_match_non_matching_in_middle(self):
        self.assertEqual(text_match_three('ababababcabab'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_three(''), 'Not matched!')

    def test_none_input(self):
        self.assertEqual(text_match_three(None), 'Not matched!')
