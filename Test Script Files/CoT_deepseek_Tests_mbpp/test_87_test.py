import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'d': 5, 'e': 6}
        expected = {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_empty_dicts(self):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        expected = {}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_one_empty_dict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        dict3 = {'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_duplicate_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'b': 5, 'd': 6}
        expected = {'a': 1, 'b': 5, 'c': 4, 'd': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            merge_dictionaries_three(123, {'a': 1}, {'b': 2})
