import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):
    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        self.assertEqual(merge_dict(d1, d2), {'a': 1, 'b': 2, 'c': 3, 'd': 4})

    def test_empty_dict(self):
        d1 = {}
        d2 = {'c': 3, 'd': 4}
        self.assertEqual(merge_dict(d1, d2), {'c': 3, 'd': 4})

    def test_update_overrides(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'd': 4}
        self.assertEqual(merge_dict(d1, d2), {'a': 1, 'b': 3, 'd': 4})

    def test_update_adds(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(merge_dict(d1, d2), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

    def test_update_overrides_with_empty(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        self.assertEqual(merge_dict(d1, d2), {'a': 1, 'b': 2})

    def test_update_adds_with_empty(self):
        d1 = {}
        d2 = {'c': 3, 'd': 4}
        self.assertEqual(merge_dict(d1, d2), {'c': 3, 'd': 4})
