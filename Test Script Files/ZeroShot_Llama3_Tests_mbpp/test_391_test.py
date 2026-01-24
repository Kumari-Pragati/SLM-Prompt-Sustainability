import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_convert_list_dictionary(self):
        l1 = ['a', 'b', 'c']
        l2 = ['1', '2', '3']
        l3 = [1, 2, 3]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'1': 1}}, {'b': {'2': 2}}, {'c': {'3': 3}}])

    def test_convert_list_dictionary_empty_list(self):
        l1 = []
        l2 = []
        l3 = []
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [])

    def test_convert_list_dictionary_single_element(self):
        l1 = ['a']
        l2 = ['1']
        l3 = [1]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'1': 1}}])

    def test_convert_list_dictionary_mismatched_lengths(self):
        l1 = ['a', 'b']
        l2 = ['1', '2', '3']
        l3 = [1, 2, 3]
        with self.assertRaises(IndexError):
            convert_list_dictionary(l1, l2, l3)
