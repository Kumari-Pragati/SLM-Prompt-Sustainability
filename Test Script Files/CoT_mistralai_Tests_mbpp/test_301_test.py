import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_value_dict(self):
        self.assertEqual(dict_depth({'key': 1}), 1)

    def test_multi_level_dict(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}), 3)

    def test_list_value_dict(self):
        self.assertEqual(dict_depth({'key': [1, 2, 3]}), 1)

    def test_tuple_value_dict(self):
        self.assertEqual(dict_depth({'key': (1, 2, 3)}), 1)

    def test_set_value_dict(self):
        self.assertEqual(dict_depth({'key': {1, 2, 3}}), 1)

    def test_none_value_dict(self):
        self.assertEqual(dict_depth({'key': None}), 1)

    def test_empty_list_value_dict(self):
        self.assertEqual(dict_depth({'key': []}), 1)

    def test_empty_tuple_value_dict(self):
        self.assertEqual(dict_depth({'key': ()}), 1)

    def test_empty_set_value_dict(self):
        self.assertEqual(dict_depth({'key': set()}), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, dict_depth, 123)
        self.assertRaises(TypeError, dict_depth, (1, 2, 3))
        self.assertRaises(TypeError, dict_depth, [1, 2, 3])
        self.assertRaises(TypeError, dict_depth, set([1, 2, 3]))
