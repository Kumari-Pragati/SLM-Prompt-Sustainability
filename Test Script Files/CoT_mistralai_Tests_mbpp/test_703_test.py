import unittest
from703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_empty_dictionary(self):
        self.assertFalse(is_key_present({}, 'key'))

    def test_present_key(self):
        self.assertTrue(is_key_present({'key': 'value'}, 'key'))

    def test_absent_key(self):
        self.assertFalse(is_key_present({'other_key': 'value'}, 'key'))

    def test_none_dictionary(self):
        self.assertFalse(is_key_present(None, 'key'))

    def test_non_string_key(self):
        self.assertRaises(TypeError, is_key_present, {'key': 'value'}, 123)

    def test_non_hashable_value(self):
        self.assertRaises(TypeError, is_key_present, {'key': [1, 2, 3]}, 'key')
