import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_same_length(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['pattern1', 'pattern2', 'pattern3']))
        self.assertFalse(is_samepatterns(['red', 'blue'], ['pattern1', 'pattern1']))

    def test_same_sets(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['pattern1', 'pattern2']))
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['pattern1', 'pattern2', 'pattern1']))

    def test_same_sequence(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'red'], ['pattern1', 'pattern2', 'pattern3']))
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['pattern1', 'pattern1', 'pattern1']))

    def test_empty_input(self):
        self.assertTrue(is_samepatterns([], []))
