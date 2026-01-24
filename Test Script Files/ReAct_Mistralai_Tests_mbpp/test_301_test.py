import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_empty_dict(self):
        """Test that an empty dictionary returns 0"""
        self.assertEqual(dict_depth({}), 0)

    def test_single_value_dict(self):
        """Test that a dictionary with a single value returns 1"""
        self.assertEqual(dict_depth({'key': 0}), 1)

    def test_multi_level_dict(self):
        """Test that a multi-level dictionary returns the correct depth"""
        complex_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': {'g': 4, 'h': {'i': 5}}}}}
        self.assertEqual(dict_depth(complex_dict), 4)

    def test_list_value_dict(self):
        """Test that a dictionary with a list value returns the correct depth"""
        list_dict = {'a': [1, {'b': 2}]}
        self.assertEqual(dict_depth(list_dict), 2)

    def test_tuple_value_dict(self):
        """Test that a dictionary with a tuple value returns the correct depth"""
        tuple_dict = {'a': (1, {'b': 2})}
        self.assertEqual(dict_depth(tuple_dict), 2)

    def test_set_value_dict(self):
        """Test that a dictionary with a set value returns the correct depth"""
        set_dict = {'a': {'b', 'c'}}
        self.assertEqual(dict_depth(set_dict), 1)

    def test_non_dict_value(self):
        """Test that a non-dictionary value returns 0"""
        non_dict_dict = {'a': 1, 'b': 'str'}
        self.assertEqual(dict_depth(non_dict_dict), 1)
