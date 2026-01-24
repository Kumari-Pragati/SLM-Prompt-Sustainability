import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):
    def test_empty_dicts(self):
        self.assertEqual(add_dict({}, {}), Counter())

    def test_single_dict(self):
        self.assertEqual(add_dict({'a': 1}, {}), Counter({'a': 1}))

    def test_equal_dicts(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'a': 1, 'b': 2}), Counter({'a': 2, 'b': 2}))

    def test_non_equal_dicts(self):
        self.assertEqual(add_dict({'a': 1, 'b': 2}, {'a': 1, 'c': 3}), Counter({'a': 2, 'b': 2, 'c': 3}))

    def test_dict_with_duplicates(self):
        self.assertEqual(add_dict({'a': 2, 'b': 2}, {'a': 1, 'b': 1}), Counter({'a': 3, 'b': 3}))

    def test_dict_with_negative_values(self):
        self.assertEqual(add_dict({'a': 2, 'b': -2}, {'a': 1, 'b': 1}), Counter({'a': 3, 'b': 0}))

    def test_dict_with_zero_values(self):
        self.assertEqual(add_dict({'a': 0, 'b': 0}, {'a': 0, 'b': 0}), Counter({'a': 0, 'b': 0}))
