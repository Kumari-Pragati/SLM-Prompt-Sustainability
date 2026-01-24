import unittest
from mbpp_263_code import deepcopy
from 263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_normal_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_edge_case_empty_dict(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_edge_case_single_key(self):
        d1 = {'a': 1}
        d2 = {'a': 2}
        expected = {'a': 2}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_edge_case_same_key(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 3, 'b': 4}
        expected = {'a': 3, 'b': 4}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_edge_case_nested_dict(self):
        d1 = {'a': {'x': 1}, 'b': 2}
        d2 = {'a': {'y': 2}, 'c': 3}
        expected = {'a': {'x': 1, 'y': 2}, 'b': 2, 'c': 3}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_edge_case_list_values(self):
        d1 = {'a': [1, 2], 'b': 2}
        d2 = {'a': [3, 4], 'c': 3}
        expected = {'a': [1, 2, 3, 4], 'b': 2, 'c': 3}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_edge_case_set_values(self):
        d1 = {'a': set([1, 2]), 'b': 2}
        d2 = {'a': set([3, 4]), 'c': 3}
        expected = {'a': set([1, 2, 3, 4]), 'b': 2, 'c': 3}
        self.assertEqual(merge_dict(d1, d2), expected)

    def test_invalid_input_type_1(self):
        with self.assertRaises(TypeError):
            merge_dict(1, 2)

    def test_invalid_input_type_2(self):
        with self.assertRaises(TypeError):
            merge_dict('str', {'key': 'value'})
