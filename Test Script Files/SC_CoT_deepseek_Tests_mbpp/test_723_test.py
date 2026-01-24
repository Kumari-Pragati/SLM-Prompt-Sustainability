import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)

    def test_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_different_lengths(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2]), 2)

    def test_mixed_types(self):
        self.assertEqual(count_same_pair([1, '2', 3], [1, '2', 3]), 2)

    def test_edge_cases(self):
        self.assertEqual(count_same_pair([0], [0]), 1)
        self.assertEqual(count_same_pair([-1], [-1]), 1)
        self.assertEqual(count_same_pair([100], [100]), 1)

    def test_special_cases(self):
        self.assertEqual(count_same_pair([1, 2, 3], [3, 2, 1]), 3)
        self.assertEqual(count_same_pair([1, 2, 3], [3, 2, 4]), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_same_pair([1, 2, 3], 'not a list')
        with self.assertRaises(TypeError):
            count_same_pair('not a list', [1, 2, 3])
        with self.assertRaises(TypeError):
            count_same_pair('not a list', 'not a list')
