import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_typical_case(self):
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

    def test_identical_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_duplicate_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_non_dict_inputs(self):
        d1 = 'not a dict'
        d2 = {'b': 3, 'c': 4}
        with self.assertRaises(TypeError):
            merge_dict(d1, d2)
