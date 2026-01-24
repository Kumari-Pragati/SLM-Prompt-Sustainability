import unittest
from mbpp_902_code import Counter
from nine_hundred_two_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_simple_addition(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 5, 'c': 4}
        self.assertDictEqual(add_dict(d1, d2), expected)

    def test_empty_dict(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertDictEqual(add_dict(d1, d2), expected)

        d1 = {'a': 1, 'b': 2}
        d2 = {}
        self.assertDictEqual(add_dict(d1, d2), d1)

    def test_duplicate_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'b': 2}
        expected = {'a': 4, 'b': 4}
        self.assertDictEqual(add_dict(d1, d2), expected)

    def test_large_dicts(self):
        d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        d2 = {'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
        self.assertDictEqual(add_dict(d1, d2), expected)
