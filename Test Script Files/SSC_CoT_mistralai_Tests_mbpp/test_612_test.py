import unittest
from mbpp_612_code import zip
from six.moves import range

from612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_normal_case(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        result = merge(data)
        expected = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        self.assertEqual(result, expected)

    def test_edge_case_empty_list(self):
        data = []
        self.assertEqual(merge(data), [])

    def test_edge_case_single_list(self):
        data = [[1]]
        result = merge(data)
        expected = [[1]]
        self.assertEqual(result, expected)

    def test_edge_case_two_lists(self):
        data = [
            [1, 2],
            [3]
        ]
        result = merge(data)
        expected = [
            [1, 3],
            [2]
        ]
        self.assertEqual(result, expected)

    def test_edge_case_two_lists_different_lengths(self):
        data = [
            [1, 2, 3],
            [1]
        ]
        result = merge(data)
        expected = [
            [1, 1],
            [2, ]
            [3, ]
        ]
        self.assertEqual(result, expected)

    def test_edge_case_two_lists_different_types(self):
        data = [
            [1, 2, 3],
            [1.0, 2.0, 3.0]
        ]
        result = merge(data)
        expected = [
            [1, 1.0],
            [2, 2.0],
            [3, 3.0]
        ]
        self.assertEqual(result, expected)
