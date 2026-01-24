import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):
    def test_typical_case(self):
        data = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]
        expected = [['a', 'b', 'c', None], ['e', 'f', None, 'h'], ['i', None, 'k', 'l']]
        self.assertEqual(remove_column(data, 2), expected)

    def test_edge_case_empty_list(self):
        data = []
        with self.assertRaises(TypeError):
            remove_column(data, 0)

    def test_edge_case_empty_column(self):
        data = [['a', 'b', None, 'd'], ['e', 'f', None, 'h'], ['i', None, None, 'l']]
        expected = [['a', 'b', None, None], ['e', 'f', None, None], ['i', None, None, None]]
        self.assertEqual(remove_column(data, 2), expected)

    def test_edge_case_negative_index(self):
        data = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]
        with self.assertRaises(ValueError):
            remove_column(data, -1)

    def test_edge_case_index_greater_than_length(self):
        data = [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']]
        with self.assertRaises(IndexError):
            remove_column(data, 4)
