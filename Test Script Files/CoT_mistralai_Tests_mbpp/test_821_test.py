import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):

    def test_empty_dictionaries(self):
        self.assertDictEqual(merge_dictionaries({}, {}), {})

    def test_single_dictionary(self):
        self.assertDictEqual(merge_dictionaries({'a': 1}, {}), {'a': 1})
        self.assertDictEqual(merge_dictionaries({}, {'a': 1}), {'a': 1})

    def test_overlapping_keys(self):
        self.assertDictEqual(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})

    def test_conflicting_values(self):
        self.assertDictEqual(merge_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'b': 4}), {'a': 3, 'b': 4})

    def test_chainmap_behavior(self):
        self.assertDictEqual(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})
        self.assertDictEqual(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'a': 4}), {'a': 4, 'b': 3})

    def test_invalid_input(self):
        self.assertRaises(TypeError, merge_dictionaries, 1, 2)
        self.assertRaises(TypeError, merge_dictionaries, {}, 1)
        self.assertRaises(TypeError, merge_dictionaries, 1, {})
