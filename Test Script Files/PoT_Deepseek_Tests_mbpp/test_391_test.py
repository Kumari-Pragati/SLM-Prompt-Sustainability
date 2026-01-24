import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_typical_case(self):
        l1 = [1, 2, 3]
        l2 = ['a', 'b', 'c']
        l3 = ['x', 'y', 'z']
        expected_output = [{1: {'a': 'x'}}, {2: {'b': 'y'}}, {3: {'c': 'z'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        expected_output = []
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_different_lengths(self):
        l1 = [1, 2]
        l2 = ['a', 'b', 'c']
        l3 = ['x', 'y', 'z']
        expected_output = [{1: {'a': 'x'}}, {2: {'b': 'y'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_single_element(self):
        l1 = [1]
        l2 = ['a']
        l3 = ['x']
        expected_output = [{1: {'a': 'x'}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)
