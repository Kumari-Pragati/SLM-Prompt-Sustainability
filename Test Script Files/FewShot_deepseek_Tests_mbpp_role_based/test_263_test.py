import unittest
from mbpp_263_code import merge_dict

class TestMergeDict(unittest.TestCase):
    def test_typical_use_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_edge_case_empty_dicts(self):
        d1 = {}
        d2 = {}
        expected = {}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_boundary_case_one_empty_dict(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_invalid_input(self):
        d1 = {'a': 1, 'b': 2}
        d2 = 'not a dictionary'
        with self.assertRaises(TypeError):
            merge_dict(d1, d2)
