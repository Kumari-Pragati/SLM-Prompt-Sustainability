import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected_result = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected_result)

    def test_empty_dicts(self):
        d1 = {}
        d2 = {}
        expected_result = {}
        self.assertEqual(merge_dict(d1, d2), expected_result)

    def test_one_empty_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        expected_result = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected_result)

    def test_duplicate_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected_result = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected_result)

    def test_non_dict_inputs(self):
        with self.assertRaises(TypeError):
            merge_dict('not a dict', {'a': 1, 'b': 2})
        with self.assertRaises(TypeError):
            merge_dict({'a': 1, 'b': 2}, 'not a dict')
