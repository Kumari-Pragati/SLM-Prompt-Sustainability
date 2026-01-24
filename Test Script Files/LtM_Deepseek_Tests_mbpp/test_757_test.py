import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'bca']), '3')
        self.assertEqual(count_reverse_pairs(['123', '321', '231']), '3')

    def test_edge_conditions(self):
        self.assertEqual(count_reverse_pairs(['']), '0')
        self.assertEqual(count_reverse_pairs(['a']), '0')
        self.assertEqual(count_reverse_pairs(['1234567890']), '0')

    def test_boundary_conditions(self):
        self.assertEqual(count_reverse_pairs(['a'*10000]), '0')

    def test_complex_cases(self):
        self.assertEqual(count_reverse_pairs(['abc', 'bca', 'cab', 'cba']), '4')
        self.assertEqual(count_reverse_pairs(['123', '312', '231', '132']), '4')
