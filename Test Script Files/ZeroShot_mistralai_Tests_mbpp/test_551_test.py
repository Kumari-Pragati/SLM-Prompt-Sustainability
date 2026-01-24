import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(IndexError, extract_column, [], 0)

    def test_single_element_list(self):
        self.assertEqual(extract_column([[1]], 0), [1])

    def test_multiple_element_lists(self):
        self.assertEqual(extract_column([[1, 'a'], [2, 'b'], [3, 'c']], 1), ['a', 'b', 'c'])

    def test_negative_index(self):
        self.assertRaises(IndexError, extract_column, [[1, 2], [3, 4]], -1)

    def test_out_of_range_index(self):
        self.assertRaises(IndexError, extract_column, [[1, 2], [3, 4]], 2)
