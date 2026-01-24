import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected_output = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected_output)

    def test_empty_dict(self):
        d1 = {}
        d2 = {'b': 3, 'c': 4}
        expected_output = {'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected_output)

    def test_same_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'c': 4}
        expected_output = {'a': 3, 'b': 2, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected_output)

    def test_same_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 2}
        expected_output = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected_output)

    def test_invalid_input(self):
        d1 = {'a': 1, 'b': 2}
        d2 = 'not a dict'
        with self.assertRaises(TypeError):
            merge_dict(d1, d2)
