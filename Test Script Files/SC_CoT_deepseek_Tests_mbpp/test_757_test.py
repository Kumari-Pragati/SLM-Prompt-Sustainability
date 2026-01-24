import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'bca']), '3')
        self.assertEqual(count_reverse_pairs(['123', '321', '231']), '3')
        self.assertEqual(count_reverse_pairs(['test', 'tset', 'sett']), '3')

    def test_edge_cases(self):
        self.assertEqual(count_reverse_pairs(['']), '0')
        self.assertEqual(count_reverse_pairs(['a']), '0')
        self.assertEqual(count_reverse_pairs(['ab', 'ba']), '2')

    def test_corner_cases(self):
        self.assertEqual(count_reverse_pairs(['123', '321', '231', '123']), '4')
        self.assertEqual(count_reverse_pairs(['test', 'tset', 'sett', 'test']), '4')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_reverse_pairs(123)
        with self.assertRaises(TypeError):
            count_reverse_pairs(['abc', 'cba', 123])
        with self.assertRaises(TypeError):
            count_reverse_pairs(['abc', 'cba', 'bca', 123])
