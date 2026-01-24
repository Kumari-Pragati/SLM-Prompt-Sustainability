import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_reverse_pairs([1, 3, 2]), '2')
        self.assertEqual(count_reverse_pairs([3, 3, 3]), '0')
        self.assertEqual(count_reverse_pairs([1, 2, 1, 0]), '2')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_reverse_pairs([]), '0')
        self.assertEqual(count_reverse_pairs([0]), '0')
        self.assertEqual(count_reverse_pairs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), '55')
        self.assertEqual(count_reverse_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), '945')

    def test_special_cases(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'a']), '2')
        self.assertEqual(count_reverse_pairs(['A', 'B', 'A']), '2')
        self.assertEqual(count_reverse_pairs(['z', 'y', 'z']), '2')
        self.assertEqual(count_reverse_pairs(['Z', 'Y', 'Z']), '2')

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_reverse_pairs, 123)
        self.assertRaises(TypeError, count_reverse_pairs, {'a': 1, 'b': 2})
