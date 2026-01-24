import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with no z"), 'Not matched!')

    def test_z_at_start(self):
        self.assertEqual(text_match_wordz_middle("z is a test with z in the middle"), 'Found a match!')

    def test_z_at_end(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z at the end"), 'Found a match!')

    def test_z_in_middle_and_start(self):
        self.assertEqual(text_match_wordz_middle("z is a test with z in the middle and start"), 'Found a match!')

    def test_z_in_middle_and_end(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle and end"), 'Found a match!')

    def test_z_not_found(self):
        self.assertEqual(text_match_wordz_middle("This is a test with no z at all"), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_wordz_middle(""), 'Not matched!')
