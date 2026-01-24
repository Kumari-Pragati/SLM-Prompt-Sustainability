import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_length(['abc', 'de', 'fghi']), (4, 'fghi'))
        self.assertEqual(max_length(['hello', 'world']), (5, 'hello'))

    def test_edge_cases(self):
        self.assertEqual(max_length(['a']), (1, 'a'))
        self.assertEqual(max_length(['']), (0, ''))

    def test_boundary_cases(self):
        self.assertEqual(max_length(['abcdefghijklmnopqrstuvwxyz', 'a']), (26, 'abcdefghijklmnopqrstuvwxyz'))
        self.assertEqual(max_length(['a'*10000, 'a']), (10000, 'a'*10000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_length(123)
        with self.assertRaises(TypeError):
            max_length(['abc', 123])
        with self.assertRaises(TypeError):
            max_length(['abc', 'def', 123])
