import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_reverse_pairs([1, 12, 3, 4, 5, 2]), '2')
        self.assertEqual(count_reverse_pairs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), '55')
        self.assertEqual(count_reverse_pairs([5, 5, 5, 5, 5]), '0')

    def test_edge_and_boundary_cases(self):
        self.assertEqual(count_reverse_pairs([]), '0')
        self.assertEqual(count_reverse_pairs([1]), '0')
        self.assertEqual(count_reverse_pairs([1, 1]), '1')
        self.assertEqual(count_reverse_pairs([1, 1, 1]), '2')
        self.assertEqual(count_reverse_pairs([1, 1, 1, 1]), '3')
        self.assertEqual(count_reverse_pairs([1, 1, 1, 1, 1]), '4')

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_reverse_pairs, [1, 'a', 3])
        self.assertRaises(TypeError, count_reverse_pairs, ['1', 2, 3])
