import unittest
from mbpp_821_code import ChainMap

def merge_dictionaries(dict1, dict2):
    merged_dict = dict(ChainMap({}, dict1, dict2))
    return merged_dict

class TestMergeDictionaries(unittest.TestCase):

    def test_empty_dictionaries(self):
        self.assertDictEqual(merge_dictionaries({}, {}), {})

    def test_single_dictionary(self):
        self.assertDictEqual(merge_dictionaries({'a': 1}, {}), {'a': 1})
        self.assertDictEqual(merge_dictionaries({}, {'a': 1}), {'a': 1})

    def test_overlapping_keys(self):
        self.assertDictEqual(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})

    def test_non_overlapping_keys(self):
        self.assertDictEqual(merge_dictionaries({'a': 1, 'b': 2}, {'d': 4, 'e': 5}), {'a': 1, 'b': 2, 'd': 4, 'e': 5})
