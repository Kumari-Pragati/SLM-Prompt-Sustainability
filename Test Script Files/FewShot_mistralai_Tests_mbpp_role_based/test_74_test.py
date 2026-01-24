import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):
    def test_same_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'R', 'B', 'B']))
        self.assertTrue(is_samepatterns(['green', 'green', 'yellow', 'yellow'], ['G', 'G', 'Y', 'Y']))

    def test_different_patterns(self):
        self.assertFalse(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'R', 'B', 'G']))
        self.assertFalse(is_samepatterns(['green', 'green', 'yellow', 'yellow'], ['G', 'R', 'Y', 'Y']))

    def test_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'R', 'B']))
        self.assertFalse(is_samepatterns(['green', 'green', 'yellow', 'yellow'], ['G', 'G', 'Y']))

    def test_empty_lists(self):
        self.assertFalse(is_samepatterns([], []))
        self.assertFalse(is_samepatterns(['red'], []))
        self.assertFalse(is_samepatterns([], ['R']))

    def test_single_element_lists(self):
        self.assertTrue(is_samepatterns(['red'], ['R']))
        self.assertTrue(is_samepatterns(['green'], ['G']))
