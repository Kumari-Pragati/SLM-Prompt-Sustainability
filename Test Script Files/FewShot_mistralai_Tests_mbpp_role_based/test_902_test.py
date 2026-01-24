import unittest
from mbpp_902_code import Counter
from ninety_two_code import add_dict

class TestAddDict(unittest.TestCase):
    def test_add_empty_dicts(self):
        self.assertEqual(add_dict({}, {}), Counter())

    def test_add_single_item_dicts(self):
        self.assertEqual(add_dict({'a': 1}, {}), {'a': 1})
        self.assertEqual(add_dict({}, {'a': 1}), {'a': 1})

    def test_add_identical_dicts(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'a': 1, 'b': 2}), {'a': 2, 'b': 2})

    def test_add_different_dicts(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_add_dict_with_none(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'c': None, 'd': 4}), {'a': 1, 'b': 2, 'c': 1, 'd': 4})

    def test_add_dict_with_list(self):
        self.assertEqual(add_dict({'a': [1, 2, 3]}, {'b': [4, 5, 6]}), {'a': Counter([1, 2, 3]), 'b': Counter([4, 5, 6])})
