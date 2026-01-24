import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):
    def test_remove_first_column(self):
        data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        result = remove_column(data, 0)
        self.assertEqual(result, [['b', 'c'], ['e', 'f'], ['h', 'i']])

    def test_remove_middle_column(self):
        data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        result = remove_column(data, 1)
        self.assertEqual(result, [['a', 'c'], ['d', 'f'], ['g', 'i']])

    def test_remove_last_column(self):
        data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        result = remove_column(data, 2)
        self.assertEqual(result, [['a', 'b'], ['d', 'e'], ['g', 'h']])

    def test_empty_list(self):
        result = remove_column([], 0)
        self.assertEqual(result, [])

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            remove_column([['a', 'b', 'c']], -1)
