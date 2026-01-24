import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):
    def test_true_key(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2}, 'a'))

    def test_false_key(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2}, 'c'))

    def test_key_present_with_empty_dict(self):
        self.assertFalse(is_key_present({}, 'a'))

    def test_key_present_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            is_key_present(123, 'a')

    def test_key_present_with_non_string_key(self):
        with self.assertRaises(TypeError):
            is_key_present({'a': 1, 'b': 2}, 123)

    def test_key_present_with_dict_with_non_string_values(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2.5}, 'a'))

    def test_key_present_with_dict_with_non_string_keys_and_values(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2.5}, 'c'))
