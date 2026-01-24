import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):
    def test_empty_dicts(self):
        d1 = {}
        d2 = {}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {})

    def test_non_empty_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_update_overrides(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})

    def test_update_adds_new_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4, 'e': 5}
        result = merge_dict(d1, d2)
        self.assertEqual(result, {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
