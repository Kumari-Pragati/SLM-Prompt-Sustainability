import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):
    def test_typical_use_case(self):
        l1 = ['a', 'b', 'c']
        l2 = [1, 2, 3]
        l3 = [4, 5, 6]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'1': 4}, 'b': {'2': 5}, 'c': {'3': 6}}])

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [])

    def test_single_element_lists(self):
        l1 = ['a']
        l2 = [1]
        l3 = [4]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'1': 4}}])

    def test_lists_of_different_lengths(self):
        l1 = ['a', 'b']
        l2 = [1, 2, 3]
        l3 = [4, 5]
        with self.assertRaises(IndexError):
            convert_list_dictionary(l1, l2, l3)
