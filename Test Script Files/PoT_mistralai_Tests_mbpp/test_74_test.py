import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_same_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['AB', 'AB', 'AB']))
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['AB', 'BA', 'AB']))
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['AB', 'AB', 'BA']))

    def test_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['AB', 'AB', 'AB']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'red'], ['AB', 'AB']))

    def test_empty_lists(self):
        self.assertTrue(is_samepatterns([], []))
        self.assertFalse(is_samepatterns([], ['AB', 'AB', 'AB']))
        self.assertFalse(is_samepatterns(['AB'], []))

    def test_single_item_lists(self):
        self.assertTrue(is_samepatterns(['red'], ['red']))
        self.assertFalse(is_samepatterns(['red'], ['blue']))

    def test_duplicate_colors(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'red'], ['AB', 'AB', 'AB']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'red', 'red'], ['AB', 'AB', 'AB', 'AB']))

    def test_duplicate_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'blue'], ['AB', 'AB']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'red'], ['AB', 'AB', 'BA']))

    def test_mixed_case(self):
        self.assertTrue(is_samepatterns(['Red', 'Blue', 'Red'], ['AB', 'AB', 'AB']))
        self.assertFalse(is_samepatterns(['Red', 'Blue', 'Red'], ['AB', 'AB', 'BA']))
