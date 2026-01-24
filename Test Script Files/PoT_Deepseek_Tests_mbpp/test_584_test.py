import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_adverbs('I am running quickly.'), '12-15: runningly')

    def test_edge_case_no_adverb(self):
        self.assertIsNone(find_adverbs('I am eating.'))

    def test_boundary_case_empty_string(self):
        self.assertIsNone(find_adverbs(''))

    def test_corner_case_multiple_adverbs(self):
        self.assertEqual(find_adverbs('I am running quickly and happily.'), '12-15: runningly')

    def test_corner_case_adverb_at_end(self):
        self.assertEqual(find_adverbs('I am happily.'), '10-15: happily')

    def test_corner_case_adverb_at_start(self):
        self.assertEqual(find_adverbs('happily I am.'), '0-5: happily')
