import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test without z"), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_wordz_middle(""), 'Not matched!')

    def test_no_z(self):
        self.assertEqual(text_match_wordz_middle("This is a test without z in the middle"), 'Not matched!')

    def test_multiple_z(self):
        self.assertEqual(text_match_wordz_middle("This is a test with multiple z in the middle"), 'Found a match!')
