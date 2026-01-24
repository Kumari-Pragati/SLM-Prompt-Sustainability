import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamepatterns(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(is_samepatterns(['red', 'green', 'blue'], ['red', 'green', 'blue']))

    def test_edge_case_equal_length(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['red', 'green', 'blue']))

    def test_edge_case_diff_length(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red', 'green']))

    def test_edge_case_single_pattern(self):
        self.assertTrue(is_samepatterns(['red','red'], ['red']))

    def test_edge_case_single_color(self):
        self.assertTrue(is_samepatterns(['red'], ['red']))

    def test_edge_case_empty_input(self):
        self.assertFalse(is_samepatterns([], []))

    def test_edge_case_empty_pattern(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], []))

    def test_edge_case_empty_color(self):
        self.assertFalse(is_samepatterns([], ['red', 'green', 'blue']))

    def test_edge_case_diff_pattern(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red', 'green', 'yellow']))

    def test_edge_case_diff_color(self):
        self.assertFalse(is_samepatterns(['red','red','red'], ['red', 'green', 'blue']))

    def test_edge_case_same_pattern(self):
        self.assertTrue(is_samepatterns(['red','red','red'], ['red','red','red']))

    def test_edge_case_same_color(self):
        self.assertTrue(is_samepatterns(['red','red','red'], ['red','red','red']))

    def test_edge_case_diff_pattern_color(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red','red','red']))

    def test_edge_case_diff_pattern_pattern(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red', 'green','red']))

    def test_edge_case_diff_pattern_pattern_color(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red','red', 'blue']))

    def test_edge_case_diff_pattern_pattern_color_pattern(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red','red', 'blue']))
