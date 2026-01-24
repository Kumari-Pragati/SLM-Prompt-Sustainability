import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_wordz_middle("zebra"), 'Found a match!')
        self.assertEqual(text_match_wordz_middle("Zebra"), 'Found a match!')
        self.assertEqual(text_match_wordz_middle("ZebraZ"), 'Not matched!')
        self.assertEqual(text_match_wordz_middle("zebraZ"), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_wordz_middle("z"), 'Found a match!')
        self.assertEqual(text_match_wordz_middle("zz"), 'Found a match!')
        self.assertEqual(text_match_wordz_middle("zzz"), 'Not matched!')
        self.assertEqual(text_match_wordz_middle("zZ"), 'Not matched!')
        self.assertEqual(text_match_wordz_middle("Z"), 'Not matched!')
