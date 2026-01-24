import unittest
from mbpp_902_code import Counter
from copy import deepcopy
from 902_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_add_dict_normal(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'b': 2, 'c': 3, 'd': 4}
        expected = {'a': 1, 'b': 4, 'c': 6, 'd': 4}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_add_dict_edge_cases(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'b': -2, 'c': 3}
        expected = {'a': 2, 'b': 0, 'c': 6}
        self.assertEqual(add_dict(d1, d2), expected)

        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'b': 2, 'c': -3}
        expected = {'a': 2, 'b': 4, 'c': 0}
        self.assertEqual(add_dict(d1, d2), expected)

        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'b': 2, 'c': None}
        expected = {'a': 2, 'b': 4, 'c': 3}
        self.assertEqual(add_dict(d1, d2), expected)

        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'b': 2, 'c': {'x': 4}}
        expected = {'a': 2, 'b': 4, 'c': {'x': 4}}
        self.assertEqual(add_dict(d1, d2), expected)

    def test_add_dict_invalid_inputs(self):
        with self.assertRaises(TypeError):
            add_dict(1, 2)

        with self.assertRaises(TypeError):
            add_dict('a', 'b')

        with self.assertRaises(TypeError):
            add_dict([1, 2], [3, 4])
