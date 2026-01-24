import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_length(['abc', 'def', 'ghi']), (3, 'abc'))
        self.assertEqual(min_length(['123', '456', '789']), (3, '123'))

    def test_edge_conditions(self):
        self.assertEqual(min_length(['']), (0, ''))
        self.assertEqual(min_length([' ']), (1, ' '))
        self.assertEqual(min_length(['a']), (1, 'a'))

    def test_complex_cases(self):
        self.assertEqual(min_length(['abc', 'de', 'ghij']), (2, 'de'))
        self.assertEqual(min_length(['1234', '56', '7890']), (2, '56'))
