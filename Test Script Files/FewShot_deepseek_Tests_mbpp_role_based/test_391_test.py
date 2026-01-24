import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):
    def test_typical_use_case(self):
        l1 = ['a', 'b', 'c']
        l2 = [1, 2, 3]
        l3 = ['x', 'y', 'z']
        expected_result = [{'a': {'1': 'x'}}, {'b': {'2': 'y'}}, {'c': {'3': 'z'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_result)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        expected_result = []
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_result)

    def test_unequal_length_lists(self):
        l1 = ['a', 'b', 'c', 'd']
        l2 = [1, 2]
        l3 = ['x', 'y']
        with self.assertRaises(ValueError):
            convert_list_dictionary(l1, l2, l3)

    def test_invalid_input(self):
        l1 = ['a', 1, 'c']
        l2 = [1, 2, 3]
        l3 = ['x', 'y', 'z']
        with self.assertRaises(TypeError):
            convert_list_dictionary(l1, l2, l3)
