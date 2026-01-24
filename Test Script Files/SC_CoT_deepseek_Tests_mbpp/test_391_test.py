import unittest

from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):

    def test_typical_case(self):
        l1 = [1, 2, 3]
        l2 = ['a', 'b', 'c']
        l3 = [4, 5, 6]
        expected_output = [{1: {'a': 4}}, {2: {'b': 5}}, {3: {'c': 6}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        expected_output = []
        self.assertEqual(convert_list_dictionary(l1, l2, l3), expected_output)

    def test_different_length_lists(self):
        l1 = [1, 2]
        l2 = ['a', 'b', 'c']
        l3 = [4, 5, 6]
        with self.assertRaises(ValueError):
            convert_list_dictionary(l1, l2, l3)

    def test_invalid_input(self):
        l1 = [1, 'two', 3]
        l2 = ['a', 'b', 'c']
        l3 = [4, 5, 6]
        with self.assertRaises(TypeError):
            convert_list_dictionary(l1, l2, l3)
