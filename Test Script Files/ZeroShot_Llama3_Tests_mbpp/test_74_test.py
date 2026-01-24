import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_is_samepatterns_true(self):
        self.assertTrue(is_samepatterns(['red', 'blue','red', 'blue'], ['red', 'blue','red', 'blue']))

    def test_is_samepatterns_false_length_mismatch(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['red', 'blue', 'blue']))

    def test_is_samepatterns_false_pattern_mismatch(self):
        self.assertFalse(is_samepatterns(['red', 'blue','red', 'blue','red'], ['red', 'blue','red', 'blue']))

    def test_is_samepatterns_false_color_mismatch(self):
        self.assertFalse(is_samepatterns(['red', 'blue','red', 'blue','red'], ['red', 'blue','red', 'blue', 'green']))

    def test_is_samepatterns_true_empty(self):
        self.assertTrue(is_samepatterns([], []))

    def test_is_samepatterns_true_single(self):
        self.assertTrue(is_samepatterns(['red'], ['red']))

    def test_is_samepatterns_true_single_color(self):
        self.assertTrue(is_samepatterns(['red','red','red'], ['red']))

    def test_is_samepatterns_true_single_pattern(self):
        self.assertTrue(is_samepatterns(['red', 'blue','red', 'blue'], ['red','red']))
