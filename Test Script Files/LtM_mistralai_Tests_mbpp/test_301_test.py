import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_simple_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2}}), 2)
        self.assertEqual(dict_depth({'a': 1, 'b': None}), 1)
        self.assertEqual(dict_depth({'a': 1}), 1)

    def test_edge_cases(self):
        self.assertEqual(dict_depth({}), 0)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': 1}}}}), 4)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': 1, 'e': 2}}}}), 4)

    def test_complex_cases(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': 1, 'f': {'g': 2}}}}}}), 5)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': 1, 'f': {'g': 2, 'h': {'i': {'j': 3}}}}}}}}), 6)
