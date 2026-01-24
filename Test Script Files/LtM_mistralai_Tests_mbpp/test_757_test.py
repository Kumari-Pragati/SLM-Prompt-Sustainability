import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(count_reverse_pairs([1, 3, 2]), '1')

    def test_edge_case_min(self):
        self.assertEqual(count_reverse_pairs([1]), '0')

    def test_edge_case_max(self):
        self.assertEqual(count_reverse_pairs([10**100, 9*10**99, 8*10**98]), str(1))

    def test_edge_case_single_reverse(self):
        self.assertEqual(count_reverse_pairs([1, '010', 2]), '1')

    def test_edge_case_multiple_reverses(self):
        self.assertEqual(count_reverse_pairs(['abc', 'bca', 'cba']), '3')

    def test_complex_case(self):
        self.assertEqual(count_reverse_pairs([1, 3, 2, 1, 3, 2, 1, 3, 2]), '6')
