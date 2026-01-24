import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['1', '2', '3']))

    def test_empty_lists(self):
        self.assertTrue(is_samepatterns([], []))

    def test_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['1', '2', '3']))

    def test_same_elements_different_order(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'red'], ['1', '2', '1']))

    def test_same_elements_same_order(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['1', '2', '1']))

    def test_different_elements_same_order(self):
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['1', '2', '3']))

    def test_same_elements_different_patterns(self):
        self.assertFalse(is_samepatterns(['red', 'red'], ['1', '1']))
