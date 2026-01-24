import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(merge_dictionaries({}, {}), {})

    def test_single_input(self):
        self.assertEqual(merge_dictionaries({'a': 1}, {}), {'a': 1})

    def test_merged_dict(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_conflicting_keys(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'c': 4}), {'a': 1, 'b': 2, 'c': 4})

    def test_chain_map_behavior(self):
        self.assertEqual(merge_dictionaries({'a': 1}, {'a': 2, 'b': 3}), {'a': 1, 'b': 3})

    def test_chain_map_behavior2(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'c': 4}), {'a': 1, 'b': 2, 'c': 4})
