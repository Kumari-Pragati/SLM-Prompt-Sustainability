import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z in the middle"), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_wordz_middle("This is a test with no z"), 'Not matched!')

    def test_edge_z_at_start(self):
        self.assertEqual(text_match_wordz_middle("z is a test with z in the middle"), 'Found a match!')

    def test_edge_z_at_end(self):
        self.assertEqual(text_match_wordz_middle("This is a test with z at the end"), 'Found a match!')

    def test_edge_z_at_start_and_end(self):
        self.assertEqual(text_match_wordz_middle("z is a test with z at the start and end"), 'Found a match!')

    def test_corner_z_at_first_and_last(self):
        self.assertEqual(text_match_wordz_middle("z is a test with z at first and last"), 'Found a match!')
