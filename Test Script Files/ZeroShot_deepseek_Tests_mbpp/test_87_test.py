import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_empty_dictionaries(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_one_value_in_each_dictionary(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {'b': 2}, {'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    def test_same_key_different_values(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {'a': 2}, {'a': 3}), {'a': 3})

    def test_same_key_same_value(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {'a': 1}, {'a': 1}), {'a': 1})

    def test_different_keys(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}), 
                         {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
