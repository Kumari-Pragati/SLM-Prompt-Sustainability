import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add_dict_to_tuple((1, 2, 3), {'a': 4}), (1, 2, 3, {'a': 4}))
        self.assertEqual(add_dict_toTuple(('a', 'b', 'c'), {'d': 1, 'e': 2}), (('a', 'b', 'c'), {'d': 1, 'e': 2}))

    def test_edge_cases(self):
        self.assertEqual(add_dict_toTuple((), {}), ((), {}))
        self.assertEqual(add_dict_toTuple((1,), {'a': 1}), (1, {'a': 1}))
        self.assertEqual(add_dict_toTuple(('a',), {'a': 1}), (('a',), {'a': 1}))

    def test_complex(self):
        self.assertEqual(add_dict_toTuple(('a', 1, {'b': 2}), {'c': 3, 'd': {'e': 4}}), (('a', 1, {'b': 2}), {'c': 3, 'd': {'e': 4}}))
        self.assertEqual(add_dict_toTuple(({'a': 1}, 2, 3), {'b': 4, 'c': {'d': 5}}), ({'a': 1}, 2, 3, {'b': 4, 'c': {'d': 5}}))
