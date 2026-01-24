import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):
    def test_empty_dictionaries(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_single_dict(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {}, {}), {'a': 1})

    def test_two_dicts(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'c': 3}, {}), {'a': 1, 'b': 2, 'c': 3})

    def test_three_dicts(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5}), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_conflicting_keys(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5}), {'a': 1, 'b': 2, 'c': 4, 'd': 5})
