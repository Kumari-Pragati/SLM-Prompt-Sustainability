import unittest
from mbpp_263_code import deepcopy

from263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_empty_dict(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_single_dict(self):
        d1 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, {}), d1)

    def test_key_conflict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4, 'a': 0}
        expected = {'a': 0, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_deep_copy(self):
        d1 = deepcopy({'a': {'b': 1, 'c': 2}})
        d2 = {'a': {'b': 3, 'd': 4}}
        expected = {'a': {'b': 3, 'c': 2}}
        self.assertEqual(merge_dict(d1, d2), expected)
