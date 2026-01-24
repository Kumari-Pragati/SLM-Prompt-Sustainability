import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_simple_merge(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_empty_dicts(self):
        d1 = {}
        d2 = {}
        expected = {}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_one_empty_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_duplicate_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3}
        expected = {'a': 1, 'b': 3}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_large_dicts(self):
        d1 = {str(i): i for i in range(1000)}
        d2 = {str(i): i for i in range(1000, 2000)}
        expected = {str(i): i for i in range(2000)}
        self.assertEqual(merge_dict(d1, d2), expected)
