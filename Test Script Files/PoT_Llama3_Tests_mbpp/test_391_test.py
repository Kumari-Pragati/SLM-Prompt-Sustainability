import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(convert_list_dictionary(['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z']), [{'a': {1: 'x'}, 'b': {2: 'y'}, 'c': {3: 'z'}}])

    def test_edge_case_empty_list(self):
        self.assertEqual(convert_list_dictionary([], [], []), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(convert_list_dictionary(['a'], [1], ['x']), [{'a': {1: 'x'}}])

    def test_edge_case_list_of_length_1(self):
        self.assertEqual(convert_list_dictionary(['a'], ['b'], ['c']), [{'a': {'b': 'c'}}])

    def test_edge_case_list_of_length_2(self):
        self.assertEqual(convert_list_dictionary(['a', 'b'], ['c', 'd'], ['e', 'f']), [{'a': {'c': 'e'}, 'b': {'d': 'f'}}])

    def test_edge_case_list_of_length_3(self):
        self.assertEqual(convert_list_dictionary(['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']), [{'a': {'d': 'g'}, 'b': {'e': 'h'}, 'c': {'f': 'i'}}])

    def test_edge_case_list_of_length_4(self):
        self.assertEqual(convert_list_dictionary(['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']), [{'a': {'e': 'i'}, 'b': {'f': 'j'}, 'c': {'g': 'k'}, 'd': {'h': 'l'}}])

    def test_edge_case_list_of_length_5(self):
        self.assertEqual(convert_list_dictionary(['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l','m', 'n', 'o']), [{'a': {'f': 'k'}, 'b': {'g': 'l'}, 'c': {'h':'m'}, 'd': {'i': 'n'}, 'e': {'j': 'o'}}])
