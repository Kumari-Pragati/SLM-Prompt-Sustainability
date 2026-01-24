import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_count_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'bca', 'def']), '2')
        self.assertEqual(count_reverse_pairs(['abc', 'bca', 'cab']), '1')
        self.assertEqual(count_reverse_pairs(['abc', 'def', 'ghi']), '0')
        self.assertEqual(count_reverse_pairs(['123', '321', '213', '312']), '3')
        self.assertEqual(count_reverse_pairs(['123', '312', '231']), '2')
