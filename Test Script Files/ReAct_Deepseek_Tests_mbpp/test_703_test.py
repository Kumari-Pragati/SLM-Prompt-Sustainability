import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_key_present(self):
        # Typical case: key is present
        self.assertTrue(is_key_present({'a': 1, 'b': 2}, 'a'))

    def test_key_absent(self):
        # Typical case: key is absent
        self.assertFalse(is_key_present({'a': 1, 'b': 2}, 'c'))

    def test_empty_dict(self):
        # Edge case: empty dictionary
        self.assertFalse(is_key_present({}, 'a'))

    def test_key_present_multiple_times(self):
        # Edge case: key present multiple times
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'a': 3}, 'a'))

    def test_key_absent_with_empty_dict(self):
        # Edge case: key absent with empty dictionary
        self.assertFalse(is_key_present({}, 'a'))

    def test_key_absent_with_none_dict(self):
        # Error case: key absent with None dictionary
        with self.assertRaises(TypeError):
            is_key_present(None, 'a')

    def test_key_absent_with_none_key(self):
        # Error case: key absent with None key
        with self.assertRaises(TypeError):
            is_key_present({'a': 1}, None)
