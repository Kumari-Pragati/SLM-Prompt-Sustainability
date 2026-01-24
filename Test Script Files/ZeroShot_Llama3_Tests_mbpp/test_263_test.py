import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_merge_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_merge_dict_empty(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_merge_dict_same(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_merge_dict_update(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)
