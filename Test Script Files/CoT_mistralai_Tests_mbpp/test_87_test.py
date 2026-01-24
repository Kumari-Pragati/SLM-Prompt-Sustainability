import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):
    def test_empty_dictionaries(self):
        self.assertDictEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_single_dictionary(self):
        self.assertDictEqual(merge_dictionaries_three({'a': 1}, {}, {}), {'a': 1})
        self.assertDictEqual(merge_dictionaries_three({}, {'a': 1}, {}), {'a': 1})
        self.assertDictEqual(merge_dictionaries_three({}, {}, {'a': 1}), {'a': 1})

    def test_two_dictionaries(self):
        self.assertDictEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {}), {'a': 1, 'b': 3, 'c': 4})
        self.assertDictEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {}, {'c': 4}), {'a': 1, 'b': 2, 'c': 4})
        self.assertDictEqual(merge_dictionaries_three({}, {'a': 1, 'b': 2}, {'c': 4}), {'a': 1, 'b': 2, 'c': 4})

    def test_overlapping_keys(self):
        self.assertDictEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}), {'a': 5, 'b': 3, 'c': 4})

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, merge_dictionaries_three, 1, 2, 3)
        self.assertRaises(TypeError, merge_dictionaries_three, {}, 1, 2)
        self.assertRaises(TypeError, merge_dictionaries_three, 1, {}, 2)
