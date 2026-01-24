import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):
    def test_valid_input(self):
        colors = ['red', 'blue','red', 'green', 'blue','red']
        patterns = ['red', 'blue','red', 'blue','red', 'blue']
        self.assertTrue(is_samepatterns(colors, patterns))

    def test_invalid_length(self):
        colors = ['red', 'blue']
        patterns = ['red', 'blue', 'blue']
        self.assertFalse(is_samepatterns(colors, patterns))

    def test_invalid_pattern(self):
        colors = ['red', 'blue','red', 'green', 'blue','red']
        patterns = ['red', 'blue','red', 'blue','red', 'yellow']
        self.assertFalse(is_samepatterns(colors, patterns))

    def test_valid_input_with_duplicates(self):
        colors = ['red', 'blue','red', 'blue','red', 'blue']
        patterns = ['red', 'blue','red', 'blue','red', 'blue']
        self.assertTrue(is_samepatterns(colors, patterns))

    def test_invalid_input_with_duplicates(self):
        colors = ['red', 'blue','red', 'blue','red', 'blue']
        patterns = ['red', 'blue','red', 'blue','red', 'yellow', 'blue']
        self.assertFalse(is_samepatterns(colors, patterns))
