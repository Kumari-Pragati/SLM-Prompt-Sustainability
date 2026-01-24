import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_length(['abc', 'def']), (3, 'def'))
        self.assertEqual(max_length(['123', '456789']), (3, '456789'))

    def test_edge_conditions(self):
        self.assertEqual(max_length(['']), (0, ''))
        self.assertEqual(max_length(['a']), (1, 'a'))
        self.assertEqual(max_length(['abc', '']), (3, 'abc'))

    def test_complex_cases(self):
        self.assertEqual(max_length(['abc', 'defghi', 'j']), (3, 'defghi'))
        self.assertEqual(max_length(['1234567890', '123', '12345678901234567890']), (20, '12345678901234567890'))
