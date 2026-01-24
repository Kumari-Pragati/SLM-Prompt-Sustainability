import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_valid_input(self):
        data = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
        self.assertEqual(extract_column(data, 1), [2, 5])

    def test_empty_list(self):
        self.assertRaises(IndexError, extract_column, [], 0)

    def test_negative_index(self):
        self.assertRaises(IndexError, extract_column, [{'a': 1}], -1)

    def test_invalid_index(self):
        self.assertRaises(IndexError, extract_column, [{'a': 1}], 3)
