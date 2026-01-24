import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_simple_merge(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), {'a': 1, 'b': 3, 'c': 4})

    def test_empty_merge(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), {'a': 1, 'b': 2})

    def test_merge_with_same_key(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'b': 4}
        self.assertEqual(merge_dict(d1, d2), {'a': 3, 'b': 4})

    def test_merge_with_list_values(self):
        d1 = {'a': [1, 2], 'b': [3, 4]}
        d2 = {'a': [5, 6], 'c': 7}
        self.assertEqual(merge_dict(d1, d2), {'a': [1, 2, 5, 6], 'b': [3, 4], 'c': 7})

    def test_merge_with_none_value(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': None}
        self.assertEqual(merge_dict(d1, d2), {'a': None, 'b': 2})
