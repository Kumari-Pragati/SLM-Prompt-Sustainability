import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):

    def test_simple_input(self):
        data = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f']
        ]
        self.assertListEqual(extract_column(data, 1), ['b', 'e'])

    def test_edge_cases(self):
        self.assertRaises(IndexError, lambda: extract_column, [['a'], 1])
        self.assertListEqual(extract_column([], 0), [])
        self.assertListEqual(extract_column([['a']], 0), ['a'])

    def test_complex_input(self):
        data = [
            ['a', None, 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', None]
        ]
        self.assertListEqual(extract_column(data, 1), ['b', 'e', 'h'])
