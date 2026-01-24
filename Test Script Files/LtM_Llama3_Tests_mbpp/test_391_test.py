import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):
    def test_simple_inputs(self):
        l1 = ['a', 'b', 'c']
        l2 = ['x', 'y', 'z']
        l3 = [1, 2, 3]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'x': 1}}, {'b': {'y': 2}}, {'c': {'z': 3}}])

    def test_empty_inputs(self):
        l1 = []
        l2 = []
        l3 = []
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [])

    def test_single_element_inputs(self):
        l1 = ['a']
        l2 = ['x']
        l3 = [1]
        result = convert_list_dictionary(l1, l2, l3)
        self.assertEqual(result, [{'a': {'x': 1}}])

    def test_invalid_inputs(self):
        l1 = ['a', 'b', 'c']
        l2 = ['x', 'y', 'z']
        l3 = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            convert_list_dictionary(l1, l2, l3)
