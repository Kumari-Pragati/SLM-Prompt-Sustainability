import unittest
from mbpp_87_code import merge_dictionaries_three

class TestMergeDictionariesThree(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(merge_dictionaries_three({}, {}, {}), {})

    def test_single_input(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {}, {}), {'a': 1})

    def test_multiple_inputs(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}), 
                         {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})

    def test_conflicting_keys(self):
        self.assertEqual(merge_dictionaries_three({'a': 1, 'b': 2}, {'a': 3, 'c': 4}, {'b': 5, 'd': 6}), 
                         {'a': 1, 'b': 2, 'c': 4, 'd': 6})

    def test_chainmap_behavior(self):
        self.assertEqual(merge_dictionaries_three({'a': 1}, {'a': 2}, {'a': 3}), {'a': 3})
