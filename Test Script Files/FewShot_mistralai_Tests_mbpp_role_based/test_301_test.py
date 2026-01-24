import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(dict_depth({}), 0)

    def test_single_value_dict(self):
        self.assertEqual(dict_depth({'key': 1}), 1)

    def test_nested_dict(self):
        self.assertEqual(dict_depth({'key1': {'key2': 2}, 'key3': {'key4': 3}}), 2)

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
