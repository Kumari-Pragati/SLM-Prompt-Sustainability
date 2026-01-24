import unittest
from mbpp_902_code import Counter
from copy import deepcopy

class TestAddDict(unittest.TestCase):

    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'b': 4, 'd': 5}
        expected = {'a': 1, 'b': 5, 'c': 3, 'd': 5}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_empty_dict(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2, 'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_single_dict(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(add_dict(d1, {}), expected)

    def test_same_dict(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        expected = {'a': 2, 'b': 4, 'c': 6}
        self.assertEqual(add_dict(d1, d1), expected)

    def test_negative_key(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'-a': 1, '-b': 2, '-c': 3}
        expected = {'a': 0, 'b': 0, 'c': 0, '-a': 2, '-b': 2, '-c': 2}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_key_with_none(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': None, 'b': 2, 'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_key_with_empty_list(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': [], 'b': 2, 'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_key_with_empty_tuple(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': (), 'b': 2, 'c': 3}
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(add_dict(d1, d2), expected)
