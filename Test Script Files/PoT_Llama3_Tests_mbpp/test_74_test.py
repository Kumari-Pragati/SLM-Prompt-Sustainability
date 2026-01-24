import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_samepatterns(['red', 'green', 'blue'], ['red', 'green', 'blue']))

    def test_edge_case_equal_length(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['red', 'green', 'blue']))

    def test_edge_case_unequal_length(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue','red'], ['red', 'green']))

    def test_edge_case_empty(self):
        self.assertFalse(is_samepatterns([], []))

    def test_edge_case_single_element(self):
        self.assertTrue(is_samepatterns(['red'], ['red']))

    def test_edge_case_single_pattern(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red']))

    def test_edge_case_single_color(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red', 'green', 'blue','red']))

    def test_corner_case_all_same(self):
        self.assertTrue(is_samepatterns(['red','red','red'], ['red','red','red']))

    def test_corner_case_all_different(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red', 'green', 'yellow']))

    def test_corner_case_repeated_colors(self):
        self.assertFalse(is_samepatterns(['red','red', 'blue'], ['red', 'green', 'blue']))

    def test_corner_case_repeated_patterns(self):
        self.assertFalse(is_samepatterns(['red','red', 'blue','red'], ['red', 'green', 'blue','red']))
