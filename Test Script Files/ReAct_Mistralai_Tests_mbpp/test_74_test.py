import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_same_patterns_same_colors(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'R', 'B', 'B']))

    def test_same_patterns_reversed_colors(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'red', 'blue'], ['R', 'B', 'R', 'B']))

    def test_same_patterns_case_insensitive(self):
        self.assertTrue(is_samepatterns(['red', 'RED', 'blue', 'BLUE'], ['r', 'R', 'b', 'B']))

    def test_different_patterns(self):
        self.assertFalse(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'G', 'B', 'B']))

    def test_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'red', 'blue'], ['R', 'R', 'B', 'B', 'G']))

    def test_empty_input(self):
        self.assertFalse(is_samepatterns([], []))

    def test_single_input(self):
        self.assertTrue(is_samepatterns(['red'], ['R']))
        self.assertFalse(is_samepatterns(['red'], ['R', 'G']))

    def test_single_pattern_multiple_colors(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['R']))
