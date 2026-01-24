import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_typical_case(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'d': 5, 'e': 6}
        expected_result = {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_result)

    def test_empty_dictionaries(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_one_empty_dictionary(self):
        dict1 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries_three({}, dict1, {}), dict1)

    def test_duplicate_keys(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'b': 5, 'd': 6}
        expected_result = {'a': 1, 'b': 5, 'c': 4, 'd': 6}
        self.assertEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_result)

    def test_same_dictionaries(self):
        dict1 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dictionaries_three(dict1, dict1, dict1), dict1)
