import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):
    def test_same_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'green', 'blue'], ['red', 'green', 'blue']))

    def test_diff_len(self):
        self.assertFalse(is_samepatterns(['red', 'green'], ['red', 'green', 'blue']))

    def test_diff_set(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red', 'green','red']))

    def test_same_pattern(self):
        self.assertTrue(is_samepatterns(['red','red','red'], ['red','red','red']))

    def test_diff_pattern(self):
        self.assertFalse(is_samepatterns(['red', 'green', 'blue'], ['red', 'blue', 'green']))

    def test_empty(self):
        self.assertTrue(is_samepatterns([], []))

    def test_single(self):
        self.assertTrue(is_samepatterns(['red'], ['red']))
