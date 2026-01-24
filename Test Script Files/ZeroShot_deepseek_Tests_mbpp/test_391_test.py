import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_convert_list_dictionary(self):
        l1 = ['a', 'b', 'c']
        l2 = ['d', 'e', 'f']
        l3 = ['g', 'h', 'i']
        expected_output = [{'a': {'d': 'g'}}, {'b': {'e': 'h'}}, {'c': {'f': 'i'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        expected_output = []
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_unequal_length_lists(self):
        l1 = ['a', 'b', 'c', 'd']
        l2 = ['e', 'f']
        l3 = ['g', 'h', 'i']
        with self.assertRaises(ValueError):
            convert_list_dictionary(l1, l2, l3)
