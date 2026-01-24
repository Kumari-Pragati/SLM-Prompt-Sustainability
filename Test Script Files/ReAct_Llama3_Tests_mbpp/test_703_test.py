import unittest
from mbpp_703_code import is_key_present

class TestIsKeyPresent(unittest.TestCase):

    def test_present(self):
        self.assertTrue(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'b'))

    def test_absent(self):
        self.assertFalse(is_key_present({'a': 1, 'b': 2, 'c': 3}, 'd'))

    def test_empty_dict(self):
        self.assertFalse(is_key_present({}, 'a'))

    def test_empty_input(self):
        self.assertFalse(is_key_present(None, 'a'))

    def test_non_dict_input(self):
        with self.assertRaises(TypeError):
            is_key_present(123, 'a')

    def test_key_with_spaces(self):
        self.assertTrue(is_key_present({'a b': 1, 'c': 2}, 'a b'))

    def test_key_with_special_chars(self):
        self.assertTrue(is_key_present({'a!@#': 1, 'c': 2}, 'a!@#'))
