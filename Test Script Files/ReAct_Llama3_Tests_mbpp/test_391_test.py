import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_convert_list_dictionary_typical(self):
        l1 = [1, 2, 3]
        l2 = ['a', 'b', 'c']
        l3 = ['x', 'y', 'z']
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'1': {'a': 'x'}}, {'2': {'b': 'y'}}, {'3': {'c': 'z'}}])

    def test_convert_list_dictionary_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [])

    def test_convert_list_dictionary_single_element_lists(self):
        l1 = [1]
        l2 = ['a']
        l3 = ['x']
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'1': {'a': 'x'}}])

    def test_convert_list_dictionary_lists_of_different_lengths(self):
        l1 = [1, 2, 3, 4]
        l2 = ['a', 'b', 'c']
        l3 = ['x', 'y']
        with self.assertRaises(IndexError):
            convert_list_dictionary(l1, l2, l3)
