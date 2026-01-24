import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):
    def test_typical_use_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'d': 5, 'e': 6}
        expected_output = {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_output)

    def test_edge_case_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        expected_output = {}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_output)

    def test_boundary_case_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        dict3 = {'c': 3, 'd': 4}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_output)

    def test_invalid_input_non_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = 'not a dictionary'
        dict3 = {'c': 3, 'd': 4}
        with self.assertRaises(TypeError):
            merge_dictionaries_three(dict1, dict2, dict3)
