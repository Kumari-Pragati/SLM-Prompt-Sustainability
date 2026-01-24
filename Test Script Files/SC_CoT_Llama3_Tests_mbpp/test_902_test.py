import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_typical_inputs(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 3, 'd': 4}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'a': 1, 'b': 2, 'c': 3, 'd': 4}))

    def test_edge_case_empty_dict(self):
        d1 = {}
        d2 = {'c': 3, 'd': 4}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'c': 3, 'd': 4}))

    def test_edge_case_single_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'a': 1, 'b': 2}))

    def test_edge_case_zero_values(self):
        d1 = {'a': 0, 'b': 0}
        d2 = {'c': 0, 'd': 0}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'a': 0, 'b': 0, 'c': 0, 'd': 0}))

    def test_edge_case_negative_values(self):
        d1 = {'a': -1, 'b': -2}
        d2 = {'c': -3, 'd': -4}
        result = add_dict(d1, d2)
        self.assertEqual(result, Counter({'a': -1, 'b': -2, 'c': -3, 'd': -4}))

    def test_invalid_input_non_dict(self):
        with self.assertRaises(TypeError):
            add_dict(123, {'a': 1, 'b': 2})

    def test_invalid_input_non_dict2(self):
        with self.assertRaises(TypeError):
            add_dict({'a': 1, 'b': 2}, 123)

    def test_invalid_input_non_dict3(self):
        with self.assertRaises(TypeError):
            add_dict(123, 456)
