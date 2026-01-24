import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(convert_list_dictionary([1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]),
                              [{'1': {'a': 4}, '2': {'b': 5}, '3': {'c': 6}}])

    def test_edge_cases(self):
        self.assertListEqual(convert_list_dictionary([], [], []), [])
        self.assertListEqual(convert_list_dictionary([1], ['a'], [4]), [{'1': {'a': 4}}])
        self.assertListEqual(convert_list_dictionary([1, 2], ['a', 'b'], [4, 5]),
                              [{'1': {'a': 4}, '2': {'b': 5}}])

    def test_complex(self):
        self.assertListEqual(convert_list_dictionary([1, 2, 3], ['a', 'b', 'c', 'd'], [4, 5, 6, 7]),
                              [{'1': {'a': 4}, '2': {'b': 5}, '3': {'c': 6, 'd': 7}}])
        self.assertListEqual(convert_list_dictionary([1, 2], ['a', 'b', 'c'], [4, 5, 6]),
                              [{'1': {'a': 4}, '2': {'b': 5, 'c': 6}}])
