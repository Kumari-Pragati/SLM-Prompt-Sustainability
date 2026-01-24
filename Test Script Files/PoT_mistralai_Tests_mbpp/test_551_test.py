import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_typical_case(self):
        data = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        result = extract_column(data, 1)
        self.assertEqual(result, ['b', 'e', 'h'])

    def test_edge_case_empty_list(self):
        data = []
        with self.assertRaises(IndexError):
            extract_column(data, 0)

    def test_edge_case_empty_column(self):
        data = [
            ['a'],
            ['b'],
            ['c']
        ]
        result = extract_column(data, 1)
        self.assertEqual(result, [])

    def test_edge_case_negative_index(self):
        data = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        with self.assertRaises(IndexError):
            extract_column(data, -1)

    def test_edge_case_out_of_range_index(self):
        data = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        with self.assertRaises(IndexError):
            extract_column(data, 3)
