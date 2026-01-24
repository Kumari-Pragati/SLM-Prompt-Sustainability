import unittest
from mbpp_263_code import deepcopy
from 263_code import merge_dict

class TestMergeDict(unittest.TestCase):

    def test_empty_dicts(self):
        """Test merging two empty dictionaries."""
        d1 = {}
        d2 = {}
        result = merge_dict(d1, d2)
        self.assertDictEqual(result, {'{}\\x000000000000000000000000}': None})  # Checks if dictionaries are properly copied and merged

    def test_single_key_dicts(self):
        """Test merging two dictionaries with a single key."""
        d1 = {'key': 'value1'}
        d2 = {'key': 'value2'}
        result = merge_dict(d1, d2)
        self.assertDictEqual(result, {'key': 'value2'})

    def test_same_key_dicts(self):
        """Test merging two dictionaries with the same key."""
        d1 = {'key': 'value1'}
        d2 = {'key': 'value2'}
        result = merge_dict(d1, d2)
        self.assertDictEqual(result, {'key': 'value2'})

    def test_different_key_dicts(self):
        """Test merging two dictionaries with different keys."""
        d1 = {'key1': 'value1'}
        d2 = {'key2': 'value2'}
        result = merge_dict(d1, d2)
        self.assertDictEqual(result, {'key1': 'value1', 'key2': 'value2'})

    def test_nested_dicts(self):
        """Test merging two dictionaries with nested dictionaries."""
        d1 = {'key1': {'nested_key': 'value1'}}
        d2 = {'key2': {'nested_key': 'value2'}}
        result = merge_dict(d1, d2)
        self.assertDictEqual(result, {'key1': {'nested_key': 'value1'}, 'key2': {'nested_key': 'value2'}})

    def test_key_error(self):
        """Test if KeyError is raised when trying to merge a dictionary with a non-existent key."""
        d1 = {'key': 'value'}
        with self.assertRaises(KeyError):
            merge_dict(d1, {'non_existent_key': 'value'})

    def test_value_error(self):
        """Test if ValueError is raised when trying to merge a dictionary with a non-hashable value."""
        d1 = {'key': [1, 2, 3]}
        with self.assertRaises(TypeError):
            merge_dict(d1, {'key': {'non_hashable_value': 'value'}})
