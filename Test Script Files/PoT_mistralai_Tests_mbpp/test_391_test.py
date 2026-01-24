import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(
            convert_list_dictionary([1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]),
            [
                {1: {'a': 4}},
                {2: {'b': 5}},
                {3: {'c': 6}}
            ]
        )

    def test_edge_case_empty_lists(self):
        self.assertListEqual(
            convert_list_dictionary([], [], []),
            []
        )

    def test_edge_case_single_list(self):
        self.assertListEqual(
            convert_list_dictionary([1], ['a'], [4]),
            [{1: {'a': 4}}]
        )

    def test_edge_case_different_lengths(self):
        self.assertListEqual(
            convert_list_dictionary([1, 2], ['a', 'b'], [4, 5]),
            [
                {1: {'a': 4}},
                {2: {'b': None}}
            ]
        )

    def test_corner_case_duplicate_keys(self):
        self.assertListEqual(
            convert_list_dictionary([1, 2], ['a', 'a'], [4, 5]),
            [
                {1: {'a': 4}},
                {2: {'a': 5}}
            ]
        )
