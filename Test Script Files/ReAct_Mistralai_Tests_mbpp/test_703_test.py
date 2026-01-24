import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_empty_dictionary(self):
        self.assertFalse(is_key_present({}, 'key'))

    def test_key_present(self):
        self.assertTrue(is_key_present({'key': 'value'}, 'key'))

    def test_key_absent(self):
        self.assertFalse(is_key_present({'other_key': 'value'}, 'key'))

    def test_key_case_sensitivity(self):
        self.assertFalse(is_key_present({'key': 'value'}, 'KEY'))

    def test_non_string_key(self):
        with self.assertRaises(TypeError):
            is_key_present({1: 'value'}, 1)

    def test_non_hashable_value(self):
        data = {'key': [1, 2, 3]}
        with self.assertRaises(TypeError):
            is_key_present(data, 'key')
