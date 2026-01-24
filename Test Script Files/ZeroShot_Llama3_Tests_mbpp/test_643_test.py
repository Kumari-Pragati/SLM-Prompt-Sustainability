import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z at the start"), 'Not matched!')

    def test_found_match_with_multiple_z(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle and another z"), 'Found a match!')

    def test_not_found_match_with_no_z(self):
        self.assertEqual(text_match_wordz_middle("This is a test with no z"), 'Not matched!')

    def test_found_match_with_z_at_the_end(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z at the end"), 'Found a match!')