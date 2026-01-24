import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):
    def test_merge_three_dictionaries(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'c': 5, 'd': 6}
        expected_result = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_result)

    def test_merge_empty_dictionaries(self):
        dict1 = {}
        dict2 = {}
        dict3 = {}
        expected_result = {}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_result)

    def test_merge_one_dictionary(self):
        dict1 = {'a': 1}
        dict2 = {}
        dict3 = {}
        expected_result = {'a': 1}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_result)

    def test_merge_two_dictionaries_one_empty(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {}
        dict3 = {}
        expected_result = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_result)

    def test_merge_two_dictionaries_one_with_empty(self):
        dict1 = {}
        dict2 = {'a': 1, 'b': 2}
        dict3 = {}
        expected_result = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_result)
