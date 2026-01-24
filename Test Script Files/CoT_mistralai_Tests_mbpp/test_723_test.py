import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_same_length_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3], [3, 2, 1]), 3)
        self.assertEqual(count_same_pair([4, 4, 4, 4], [4, 4, 4, 4]), 4)
        self.assertEqual(count_same_pair([], []), 0)

    def test_different_length_lists(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2]), 2)
        self.assertEqual(count_same_pair([1, 2], [1, 2, 3]), 1)
        self.assertEqual(count_same_pair([1], []), 0)
        self.assertEqual(count_same_pair([], [1]), 0)

    def test_no_matches(self):
        self.assertEqual(count_same_pair([1, 2, 3], [4, 5, 6]), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_same_pair, 1, 2)
        self.assertRaises(TypeError, count_same_pair, ['a', 'b'], [1, 2])
