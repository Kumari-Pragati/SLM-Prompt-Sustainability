import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):

    def test_empty_dicts(self):
        """Test adding two empty dictionaries"""
        result = add_dict({}, {})
        self.assertDictEqual(result, {})

    def test_single_key_dicts(self):
        """Test adding two dictionaries with a single key"""
        result = add_dict({'key': 1}, {'key': 2})
        self.assertDictEqual(result, {'key': 3})

    def test_same_key_dicts(self):
        """Test adding two dictionaries with the same key"""
        result = add_dict({'key': 1, 'other_key': 2}, {'key': 3, 'other_key': 4})
        self.assertDictEqual(result, {'key': 4, 'other_key': 6})

    def test_different_key_dicts(self):
        """Test adding two dictionaries with different keys"""
        result = add_dict({'key1': 1, 'key2': 2}, {'key3': 3, 'key4': 4})
        self.assertDictEqual(result, {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4})

    def test_negative_key_dict(self):
        """Test adding a dictionary with negative keys"""
        result = add_dict({-1: 'a', 0: 'b'}, {'c': 1, 'd': 2})
        self.assertDictEqual(result, {'-1': 'a', 0: 'b', 'c': 1, 'd': 2})

    def test_key_with_none_value(self):
        """Test adding a dictionary with a key with None value"""
        result = add_dict({'key': None}, {'key': 1})
        self.assertDictEqual(result, {'key': 2})

    def test_key_with_non_hashable_value(self):
        """Test adding a dictionary with a key with a non-hashable value"""
        with self.assertRaises(TypeError):
            add_dict({'key': list}, {'key': 1})
