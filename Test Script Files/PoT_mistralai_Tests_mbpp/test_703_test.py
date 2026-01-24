import unittest
from703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_present_in_dict(self):
        self.assertTrue(is_key_present({1: 'a', 2: 'b'}, 1))
        self.assertTrue(is_key_present({'a': 1, 'b': 2}, 'a'))

    def test_absent_in_dict(self):
        self.assertFalse(is_key_present({1: 'a', 2: 'b'}, 3))
        self.assertFalse(is_key_present({'a': 1, 'b': 2}, 'c'))

    def test_empty_dict(self):
        self.assertFalse(is_key_present({}, 1))
        self.assertFalse(is_key_present({}, 'a'))

    def test_none_dict(self):
        self.assertFalse(is_key_present(None, 1))
        self.assertFalse(is_key_present(None, 'a'))

    def test_key_is_none(self):
        self.assertFalse(is_key_present({1: 'a'}, None))
        self.assertFalse(is_key_present({'a': 1}, None))

    def test_key_is_empty_string(self):
        self.assertFalse(is_key_present({1: 'a'}, ''))
        self.assertFalse(is_key_present({'a': 1}, ''))
