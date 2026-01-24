import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_empty_lists(self):
        self.assertFalse(is_samepatterns([], []))

    def test_single_element_lists(self):
        self.assertTrue(is_samepatterns(['red'], ['red']))

    def test_lists_of_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'blue'], ['red']))

    def test_lists_with_duplicates(self):
        self.assertTrue(is_samepatterns(['red', 'blue','red'], ['red', 'blue','red']))

    def test_lists_with_no_duplicates(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['red', 'blue', 'green']))

    def test_lists_with_no_duplicates_and_no_order(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['green', 'blue','red']))

    def test_lists_with_duplicates_and_no_order(self):
        self.assertTrue(is_samepatterns(['red', 'blue','red', 'blue'], ['blue','red', 'blue','red']))

    def test_lists_with_duplicates_and_order(self):
        self.assertFalse(is_samepatterns(['red', 'blue','red', 'blue'], ['red', 'blue', 'blue','red']))
