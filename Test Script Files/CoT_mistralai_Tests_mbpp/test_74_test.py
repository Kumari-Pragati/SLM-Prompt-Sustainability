import unittest
from74_code import is_samepatterns

class TestIsSamepatterns(unittest.TestCase):

    def test_same_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['AB', 'AB', 'AB']))
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['AB', 'CD', 'EF']))

    def test_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['AB', 'CD']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['AB', 'CD', 'EF', 'GH']))

    def test_empty_inputs(self):
        self.assertFalse(is_samepatterns([], []))
        self.assertFalse(is_samepatterns(['red'], []))
        self.assertFalse(is_samepatterns([], ['AB']))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_samepatterns, [1, 2, 3], ['AB', 'CD'])
        self.assertRaises(TypeError, is_samepatterns, ['red', 'blue', 'green'], [1, 2, 3])
        self.assertRaises(TypeError, is_samepatterns, ['red', 'blue', 'green'], ['AB', 2])
