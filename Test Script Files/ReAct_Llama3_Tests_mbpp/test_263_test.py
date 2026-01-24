import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_merge_dict_typical(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_merge_dict_empty(self):
        d1 = {}
        d2 = {'c': 3, 'd': 4}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'c': 3, 'd': 4})

    def test_merge_dict_empty2(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_merge_dict_update(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})

    def test_merge_dict_update2(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'c': 4}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 3, 'b': 2, 'c': 4})
