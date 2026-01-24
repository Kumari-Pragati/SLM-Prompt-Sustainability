import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):
    def test_typical_inputs(self):
        l1 = ['a', 'b', 'c']
        l2 = ['x', 'y', 'z']
        l3 = [1, 2, 3]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'x': 1}}, {'b': {'y': 2}}, {'c': {'z': 3}}])

    def test_edge_cases(self):
        l1 = []
        l2 = []
        l3 = []
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [])

    def test_single_element_lists(self):
        l1 = ['a']
        l2 = ['x']
        l3 = [1]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'x': 1}}])

    def test_invalid_inputs(self):
        l1 = 'a'
        l2 = ['x']
        l3 = [1]
        with self.assertRaises(TypeError):
            convert_list_dictionary(l1, l2, l3)

    def test_mismatched_list_lengths(self):
        l1 = ['a', 'b']
        l2 = ['x', 'y', 'z']
        l3 = [1, 2, 3]
        with self.assertRaises(IndexError):
            convert_list_dictionary(l1, l2, l3)
