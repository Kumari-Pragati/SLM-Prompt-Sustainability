import unittest
from mbpp_551_code import extract_column

class TestExtractColumn(unittest.TestCase):
    def test_normal_input(self):
        data = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}]
        expected = [1, 4]
        self.assertListEqual(extract_column(data, 0), expected)

    def test_edge_and_boundary_conditions(self):
        data = [{'a': 1}, {'b': 2}]
        self.assertListEqual(extract_column(data, 0), [1, None])
        self.assertListEqual(extract_column(data, 1), [None, 2])
        self.assertListEqual(extract_column(data, 2), [None, None])

        data = [{'a': 1}, {'b': 2}, {'c': 3}]
        self.assertListEqual(extract_column(data, 0), [1, None, None])
        self.assertListEqual(extract_column(data, 1), [None, 2, None])
        self.assertListEqual(extract_column(data, 2), [None, None, 3])
        self.assertListEqual(extract_column(data, 3), [None, None, None])

        data = [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}]
        self.assertListEqual(extract_column(data, 0), [1, None, None, None])
        self.assertListEqual(extract_column(data, 1), [None, 2, None, None])
        self.assertListEqual(extract_column(data, 2), [None, None, 3, None])
        self.assertListEqual(extract_column(data, 3), [None, None, None, 4])
