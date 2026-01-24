import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):
    def test_typical_input(self):
        test_dict = {'a': 1, 'c': 3, 'b': 2}
        result = sort_dict_item(test_dict)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3})

    def test_edge_case_empty_dict(self):
        test_dict = {}
        result = sort_dict_item(test_dict)
        self.assertEqual(result, {})

    def test_edge_case_single_key_dict(self):
        test_dict = {'a': 1}
        result = sort_dict_item(test_dict)
        self.assertEqual(result, {'a': 1})

    def test_edge_case_multiple_keys_dict(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        result = sort_dict_item(test_dict)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_edge_case_dict_with_negative_values(self):
        test_dict = {'a': -1, 'b': -2, 'c': -3, 'd': -4}
        result = sort_dict_item(test_dict)
        self.assertEqual(result, {'d': -4, 'c': -3, 'b': -2, 'a': -1})

    def test_edge_case_dict_with_zero_value(self):
        test_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        result = sort_dict_item(test_dict)
        self.assertEqual(result, {'a': 0, 'b': 1, 'c': 2, 'd': 3})

    def test_edge_case_dict_with_non_numeric_values(self):
        test_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
        with self.assertRaises(TypeError):
            sort_dict_item(test_dict)
