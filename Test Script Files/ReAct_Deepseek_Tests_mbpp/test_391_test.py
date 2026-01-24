import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_typical_case(self):
        l1 = [1, 2, 3]
        l2 = ['a', 'b', 'c']
        l3 = ['x', 'y', 'z']
        expected_result = [{1: {'a': 'x'}}, {2: {'b': 'y'}}, {3: {'c': 'z'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_result)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        expected_result = []
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_result)

    def test_single_element_lists(self):
        l1 = [1]
        l2 = ['a']
        l3 = ['x']
        expected_result = [{1: {'a': 'x'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_result)

    def test_unequal_length_lists(self):
        l1 = [1, 2, 3, 4]
        l2 = ['a', 'b', 'c']
        l3 = ['x', 'y', 'z']
        with self.assertRaises(ValueError):
            convert_list_dictionary(l1, l2, l3)
