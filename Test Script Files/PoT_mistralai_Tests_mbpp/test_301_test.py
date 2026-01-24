import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_value_dict(self):
        self.assertEqual(dict_depth({'key': 1}), 1)

    def test_multi_level_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}), 3)

    def test_dict_with_list(self):
        self.assertEqual(dict_depth({'key': [1, 2, 3], 'value': {'nested': 4}}), 2)

    def test_dict_with_tuple(self):
        self.assertEqual(dict_depth({('key',): 1, ('value',): {'nested': 2}}), 1)

    def test_dict_with_set(self):
        self.assertEqual(dict_depth({set([1, 2, 3]), frozenset([4, 5, 6])}), 0)

    def test_dict_with_none(self):
        self.assertEqual(dict_depth({'key': None}), 1)

    def test_dict_with_function(self):
        def func():
            pass
        self.assertEqual(dict_depth({'key': func}), 1)
