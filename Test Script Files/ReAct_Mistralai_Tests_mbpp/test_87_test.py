import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_empty_dicts(self):
        self.assertDictEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_single_dict(self):
        self.assertDictEqual(merge_dictionaries_three({'a': 1}, {}, {}), {'a': 1})
        self.assertDictEqual(merge_dictionaries_three({}, {'a': 1}, {}), {'a': 1})
        self.assertDictEqual(merge_dictionaries_three({}, {}, {'a': 1}), {'a': 1})

    def test_two_identical_dicts(self):
        self.assertDictEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {}), {'a': 1, 'b': 2})

    def test_two_overlapping_dicts(self):
        self.assertDictEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {}), {'a': 1, 'b': 3, 'c': 4})

    def test_two_non_overlapping_dicts(self):
        self.assertDictEqual(merge_dictionaries_three({'a': 1}, {'b': 2, 'c': 4}, {}), {'a': 1, 'b': 2, 'c': 4})

    def test_one_dict_with_key_error(self):
        with self.assertRaises(KeyError):
            merge_dictionaries_three({'a': 1}, {'b': 2}, {'a': 'error'})

    def test_two_dicts_with_key_error(self):
        with self.assertRaises(KeyError):
            merge_dictionaries_three({'a': 1}, {'b': 2}, {'a': 'error', 'c': 'value'})
