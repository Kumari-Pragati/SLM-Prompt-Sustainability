import unittest
from mbpp_74_code import is_samepatterns

class TestIsSamePatterns(unittest.TestCase):

    def test_same_patterns(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'R', 'B', 'B']))
        self.assertTrue(is_samepatterns(['green', 'green', 'yellow', 'yellow'], ['G', 'G', 'Y', 'Y']))

    def test_mixed_case(self):
        self.assertTrue(is_samepatterns(['red', 'red', 'BLUE', 'blue'], ['R', 'R', 'B', 'B']))
        self.assertTrue(is_samepatterns(['green', 'GREEN', 'yellow', 'YELLOW'], ['G', 'g', 'Y', 'y']))

    def test_empty_lists(self):
        self.assertFalse(is_samepatterns([], []))
        self.assertFalse(is_samepatterns(['red'], []))
        self.assertFalse(is_samepatterns([], ['R']))

    def test_different_lengths(self):
        self.assertFalse(is_samepatterns(['red', 'red', 'blue'], ['R', 'R', 'B', 'G']))
        self.assertFalse(is_samepatterns(['red', 'red', 'blue', 'blue'], ['R', 'R', 'B', 'G', 'Y']))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_samepatterns, [1, 2, 3], ['R', 'R', 'B', 'B'])
        self.assertRaises(TypeError, is_samepatterns, ['R', 'R', 'B', 'B'], [1, 2, 3])
        self.assertRaises(TypeError, is_samepatterns, ['R', 'R', 'B', 'B'], [1, 'B', 3])
