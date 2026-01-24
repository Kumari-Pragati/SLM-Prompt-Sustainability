import unittest
from mbpp_821_code import merge_dictionaries

class TestMergeDictionaries(unittest.TestCase):
    def test_empty_dictionaries(self):
        self.assertEqual(merge_dictionaries({}, {}), {})

    def test_single_dict(self):
        self.assertEqual(merge_dictionaries({'a': 1}, {}), {'a': 1})

    def test_multiple_dicts(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_conflicting_keys(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'a': 3, 'c': 4}), {'a': 1, 'b': 2, 'c': 4})

    def test_chainmap_order(self):
        self.assertEqual(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})
