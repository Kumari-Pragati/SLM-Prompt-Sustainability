import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):
    def test_simple_addition(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 5, 'c': 4}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_empty_dicts(self):
        d1 = {}
        d2 = {}
        expected = {}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_one_empty_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_same_keys_different_values(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'b': 4}
        expected = {'a': 4, 'b': 6}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_same_values_different_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 1, 'd': 2}
        expected = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
        self.assertEqual(add_dict(d1, d2), expected)
