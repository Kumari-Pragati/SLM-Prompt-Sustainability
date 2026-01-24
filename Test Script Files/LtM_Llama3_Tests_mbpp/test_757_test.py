import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_reverse_pairs([1, 2, 3]), '3')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c']), '3')
        self.assertEqual(count_reverse_pairs([1, 2, 3, 4]), '6')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd']), '6')

    def test_empty(self):
        self.assertEqual(count_reverse_pairs([]), '0')
        self.assertEqual(count_reverse_pairs(['']), '0')

    def test_single(self):
        self.assertEqual(count_reverse_pairs([1]), '0')
        self.assertEqual(count_reverse_pairs(['a']), '0')

    def test_edge(self):
        self.assertEqual(count_reverse_pairs([1, 1]), '1')
        self.assertEqual(count_reverse_pairs(['a', 'a']), '1')
        self.assertEqual(count_reverse_pairs([1, 2, 3, 2, 1]), '3')
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'b', 'a']), '3')

    def test_invalid(self):
        with self.assertRaises(TypeError):
            count_reverse_pairs(None)
        with self.assertRaises(TypeError):
            count_reverse_pairs(123)
