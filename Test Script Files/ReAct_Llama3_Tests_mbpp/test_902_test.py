import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):
    def test_empty_dicts(self):
        self.assertEqual(add_dict({}, {}), Counter())

    def test_single_dict(self):
        self.assertEqual(add_dict({'a': 1}, {}), Counter({'a': 1}))

    def test_two_dicts(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'a': 3, 'c': 4}), Counter({'a': 4, 'b': 2, 'c': 4}))

    def test_dict_with_duplicates(self):
        self.assertEqual(add_dict({'a': 1, 'a': 2, 'b': 3}, {'a': 4, 'c': 5}), Counter({'a': 6, 'b': 3, 'c': 5}))

    def test_dict_with_negative_values(self):
        self.assertEqual(add_dict({'a': 1, 'b': -2}, {'a': -3, 'c': 4}), Counter({'a': -2, 'b': -2, 'c': 4}))

    def test_dict_with_zero_values(self):
        self.assertEqual(add_dict({'a': 0, 'b': 0}, {'a': 0, 'c': 0}), Counter({'a': 0, 'b': 0, 'c': 0}))
