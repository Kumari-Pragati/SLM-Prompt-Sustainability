import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):
    def test_typical_input(self):
        dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        self.assertEqual(sorted_dict(dict1), {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})

    def test_edge_case_empty_dict(self):
        dict1 = {}
        self.assertEqual(sorted_dict(dict1), {})

    def test_edge_case_single_key_dict(self):
        dict1 = {'a': [1, 2, 3]}
        self.assertEqual(sorted_dict(dict1), {'a': [1, 2, 3]})

    def test_edge_case_dict_with_single_value_list(self):
        dict1 = {'a': [1]}
        self.assertEqual(sorted_dict(dict1), {'a': [1]})

    def test_edge_case_dict_with_empty_list(self):
        dict1 = {'a': []}
        self.assertEqual(sorted_dict(dict1), {'a': []})

    def test_edge_case_dict_with_single_key_value(self):
        dict1 = {'a': 'hello'}
        self.assertEqual(sorted_dict(dict1), {'a': ['hello']})

    def test_edge_case_dict_with_multiple_key_value(self):
        dict1 = {'a': 'hello', 'b': 'world'}
        self.assertEqual(sorted_dict(dict1), {'a': ['hello'], 'b': ['world']})

    def test_edge_case_dict_with_non_list_values(self):
        dict1 = {'a': 'hello', 'b': 123}
        with self.assertRaises(TypeError):
            sorted_dict(dict1)

    def test_edge_case_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            sorted_dict('not a dict')
