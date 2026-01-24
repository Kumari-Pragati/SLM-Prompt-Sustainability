import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):

    def test_normal_input(self):
        data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        expected = [['a', 'b', 'c'], ['d', None, 'f'], ['g', None, 'i']]
        self.assertEqual(remove_column(data, 1), expected)

    def test_edge_cases(self):
        data = [['a', 'b', 'c'], ['d', None, 'f'], ['g', None, None]]
        expected = [['a', 'b', 'c'], ['d', None, None], ['g', None, None]]
        self.assertEqual(remove_column(data, 1), expected)

        data = [['a', None, 'c'], ['d', None, 'f'], ['g', None, None]]
        expected = [['a', None, 'c'], ['d', None, 'f'], ['g', None, None]]
        self.assertEqual(remove_column(data, 1), expected)

        data = [['a', 'b', None], ['d', None, 'f'], ['g', None, None]]
        expected = [['a', 'b', None], ['d', None, 'f'], ['g', None, None]]
        self.assertEqual(remove_column(data, 1), expected)

    def test_empty_list(self):
        data = []
        expected = []
        self.assertEqual(remove_column(data, 0), expected)

    def test_negative_index(self):
        data = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        with self.assertRaises(IndexError):
            remove_column(data, -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_column('invalid_input', 0)
