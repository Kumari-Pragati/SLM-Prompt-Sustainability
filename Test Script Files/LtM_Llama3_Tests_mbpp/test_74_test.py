import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['red', 'blue', 'green']))

    def test_empty_inputs(self):
        self.assertFalse(is_samepatterns([], []))
        self.assertFalse(is_samepatterns(['red'], []))

    def test_single_pattern(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['red', 'blue', 'green']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['red', 'blue']))

    def test_pattern_length_mismatch(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'green', 'yellow'], ['red', 'blue', 'green']))

    def test_pattern_values_mismatch(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'green', 'yellow'], ['red', 'blue','red']))

    def test_pattern_values_match(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green', 'yellow'], ['red', 'blue', 'yellow']))

    def test_pattern_values_match_with_duplicates(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'blue', 'green', 'green'], ['red', 'blue', 'blue', 'green', 'green']))
