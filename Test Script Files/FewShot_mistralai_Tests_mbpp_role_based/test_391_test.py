import unittest
from mbpp_391_code import convert_list_dictionary

class TestConvertListDictionary(unittest.TestCase):
    def test_typical_use_case(self):
        l1 = ['a', 'b', 'c']
        l2 = ['x', 'y', 'z']
        l3 = [1, 2, 3]
        result = [{'a': {'x': 1}, 'b': {'y': 2}, 'c': {'z': 3}}]
        self.assertEqual(convert_list_dictionary(l1, l2, l3), result)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        l3 = []
        result = []
        self.assertEqual(convert_list_dictionary(l1, l2, l3), result)

    def test_different_lengths(self):
        l1 = ['a', 'b', 'c']
        l2 = ['x', 'y']
        l3 = [1, 2]
        with self.assertRaises(ValueError):
            convert_list_dictionary(l1, l2, l3)

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            convert_list_dictionary([1, 2, 3], [1, 2], [1, 2, 3])
