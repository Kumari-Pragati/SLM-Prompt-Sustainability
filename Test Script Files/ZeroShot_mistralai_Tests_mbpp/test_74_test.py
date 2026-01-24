import unittest
from74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(is_samepatterns([], []))

    def test_single_element_lists(self):
        self.assertTrue(is_samepatterns(['red'], ['R', 'R']))
        self.assertFalse(is_samepatterns(['red'], ['R', 'blue']))

    def test_multiple_elements_lists(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'red'], ['R', 'B', 'R']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'red'], ['R', 'R', 'B']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'red'], ['R', 'B', 'G']))

    def test_duplicate_elements_lists(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'blue'], ['R', 'R', 'B']))
        self.assertFalse(is_samepatterns(['red', 'red', 'blue'], ['R', 'B', 'B']))

    def test_mixed_case_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'blue', 'green'], ['r', 'B', 'G']))
        self.assertFalse(is_samepatterns(['red', 'blue', 'green'], ['R', 'B', 'G']))

    def test_invalid_input(self):
        self.assertFalse(is_samepatterns([1, 2, 3], ['R', 'B', 'G']))
        self.assertFalse(is_samepatterns(['red'], [1, 2, 3]))
