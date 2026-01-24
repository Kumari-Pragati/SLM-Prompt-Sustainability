import unittest
from mbpp_679_code import access_key

class TestAccessKey(unittest.TestCase):
    def test_access_key_in_dict(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(access_key(dictionary, 'b'), 2)

    def test_access_key_out_of_dict(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(KeyError):
            access_key(dictionary, 'd')

    def test_access_key_non_dict(self):
        with self.assertRaises(TypeError):
            access_key(123, 'a')

    def test_access_key_non_string_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(TypeError):
            access_key(dictionary, 123)

    def test_access_key_non_dict_key(self):
        dictionary = {'a': 1, 'b': 2, 'c': 3}
        with self.assertRaises(TypeError):
            access_key(dictionary, None)
