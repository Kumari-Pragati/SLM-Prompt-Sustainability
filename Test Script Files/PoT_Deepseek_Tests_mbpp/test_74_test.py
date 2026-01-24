import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_samepatterns(['red', 'green', 'blue'], ['circle', 'square', 'triangle']))

    def test_edge_case_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['circle', 'square', 'triangle']))

    def test_boundary_case_empty_lists(self):
        self.assertTrue(is_samepatterns([], []))

    def test_corner_case_repeated_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'red'], ['circle', 'circle']))

    def test_corner_case_repeated_colors(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['circle', 'circle', 'triangle']))

    def test_corner_case_different_colors_same_patterns(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['circle', 'square']))

    def test_corner_case_same_colors_different_patterns(self):
        self.assertFalse(is_samepatterns(['red', 'red'], ['circle', 'triangle']))
