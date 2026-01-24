import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_simple_same_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'R', 'B', 'B']))
        self.assertTrue(is_samepatterns(['green', 'green', 'green', 'green'], ['G', 'G', 'G', 'G']))

    def test_simple_different_patterns(self):
        self.assertFalse(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'B', 'R', 'B']))
        self.assertFalse(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'B', 'G', 'G']))

    def test_edge_empty_inputs(self):
        self.assertFalse(is_samepatterns([], []))
        self.assertFalse(is_samepatterns(['red'], []))
        self.assertFalse(is_samepatterns([], ['R']))

    def test_edge_single_element(self):
        self.assertTrue(is_samepatterns(['red'], ['R']))

    def test_edge_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['R', 'B', 'G']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['R', 'B']))
