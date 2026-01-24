import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'bca']), '3')
        self.assertEqual(count_reverse_pairs(['123', '321', '231']), '3')
        self.assertEqual(count_reverse_pairs(['test', 'tset', 'sett']), '3')

    def test_edge_cases(self):
        self.assertEqual(count_reverse_pairs(['a', 'a']), '1')
        self.assertEqual(count_reverse_pairs(['1', '1']), '1')
        self.assertEqual(count_reverse_pairs(['']), '0')

    def test_boundary_conditions(self):
        self.assertEqual(count_reverse_pairs(['a'*10000], '10000')
        self.assertEqual(count_reverse_pairs(['1'*10000], '10000')

    def test_corner_cases(self):
        self.assertEqual(count_reverse_pairs(['ab', 'ba', 'abc', 'cba', 'bca']), '3')
        self.assertEqual(count_reverse_pairs(['12', '21', '123', '321', '231']), '3')
        self.assertEqual(count_reverse_pairs(['te', 'et', 'test', 'tset', 'sett']), '3')
