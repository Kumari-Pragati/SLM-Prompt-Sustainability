import unittest
from mbpp_662_code import sorted_dict

class TestSortedDict(unittest.TestCase):
    def test_typical_case(self):
        dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        self.assertEqual(sorted_dict(dict1), {'a': [1, 2, 3], 'b': [4, 5, 6]})

    def test_edge_case_empty_dict(self):
        dict1 = {}
        self.assertEqual(sorted_dict(dict1), {})

    def test_edge_case_single_key(self):
        dict1 = {'a': [1, 2, 3]}
        self.assertEqual(sorted_dict(dict1), {'a': [1, 2, 3]})

    def test_edge_case_single_key_empty_value(self):
        dict1 = {'a': []}
        self.assertEqual(sorted_dict(dict1), {'a': []})

    def test_edge_case_single_key_single_element_value(self):
        dict1 = {'a': [1]}
        self.assertEqual(sorted_dict(dict1), {'a': [1]})

    def test_edge_case_single_key_multiple_elements_value(self):
        dict1 = {'a': [1, 2, 3, 4, 5]}
        self.assertEqual(sorted_dict(dict1), {'a': [1, 2, 3, 4, 5]})

    def test_edge_case_multiple_keys(self):
        dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        self.assertEqual(sorted_dict(dict1), {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})

    def test_edge_case_multiple_keys_empty_values(self):
        dict1 = {'a': [], 'b': [], 'c': []}
        self.assertEqual(sorted_dict(dict1), {'a': [], 'b': [], 'c': []})

    def test_edge_case_multiple_keys_single_element_values(self):
        dict1 = {'a': [1], 'b': [2], 'c': [3]}
        self.assertEqual(sorted_dict(dict1), {'a': [1], 'b': [2], 'c': [3]})

    def test_edge_case_multiple_keys_multiple_elements_values(self):
        dict1 = {'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10], 'c': [11, 12, 13, 14, 15]}
        self.assertEqual(sorted_dict(dict1), {'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10], 'c': [11, 12, 13, 14, 15]})
