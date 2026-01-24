import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):
    def test_typical_case(self):
        colors = ['red', 'blue', 'green']
        patterns = ['circle', 'square', 'triangle']
        self.assertTrue(is_samepatterns(colors, patterns))

    def test_edge_case_different_lengths(self):
        colors = ['red', 'blue']
        patterns = ['circle', 'square', 'triangle']
        self.assertFalse(is_samepatterns(colors, patterns))

    def test_boundary_case_empty_lists(self):
        colors = []
        patterns = []
        self.assertTrue(is_samepatterns(colors, patterns))

    def test_invalid_input_different_lengths(self):
        colors = ['red', 'blue', 'green']
        patterns = ['circle', 'square']
        with self.assertRaises(AssertionError):
            is_samepatterns(colors, patterns)

    def test_error_handling_different_types(self):
        colors = ['red', 123]
        patterns = ['circle', 'square']
        with self.assertRaises(TypeError):
            is_samepatterns(colors, patterns)
