import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z at the start"), 'Not matched!')

    def test_found_match_at_start(self):
        self.assertEqual(text_match_wordz_middle("z is a test with z in the middle"), 'Found a match!')

    def test_found_match_at_end(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle z"), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_wordz_middle(""), 'Not matched!')

    def test_no_z(self):
        self.assertEqual(text_match_wordz_middle("This is a test with no z"), 'Not matched!')
