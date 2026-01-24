import unittest
from mbpp_87_code import ChainMap
from copy import deepcopy

def merge_dictionaries_three(dict1, dict2, dict3):
    merged_dict = dict(ChainMap({}, dict1, dict2, dict3))
    return merged_dict

class TestMergeDictionariesThree(unittest.TestCase):

    def test_empty_dicts(self):
        self.assertDictEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_single_dict(self):
        single_dict = {'a': 1, 'b': 2}
        self.assertDictEqual(merge_dictionaries_three({}, single_dict, {}), single_dict)
        self.assertDictEqual(merge_dictionaries_three(single_dict, {}, {}), single_dict)
        self.assertDictEqual(merge_dictionaries_three({}, {}, single_dict), single_dict)

    def test_two_dicts(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected_dict = {'a': 1, 'b': 3, 'c': 4}
        self.assertDictEqual(merge_dictionaries_three(dict1, dict2, {}), expected_dict)
        self.assertDictEqual(merge_dictionaries_three(dict2, dict1, {}), expected_dict)

    def test_two_dicts_conflict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'a': 4}
        expected_dict = {'a': 4, 'b': 3}
        self.assertDictEqual(merge_dictionaries_three(dict1, dict2, {}), expected_dict)
        self.assertDictEqual(merge_dictionaries_three(dict2, dict1, {}), expected_dict)

    def test_three_dicts_conflict(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        dict3 = {'a': 5, 'b': 6}
        expected_dict = {'a': 5, 'b': 6, 'c': 4}
        self.assertDictEqual(merge_dictionaries_three(dict1, dict2, dict3), expected_dict)
