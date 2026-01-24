import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):

    def test_typical_input(self):
        dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(get_key(dict), ['a', 'b', 'c'])

    def test_empty_dict(self):
        dict = {}
        self.assertEqual(get_key(dict), [])

    def test_single_key_dict(self):
        dict = {'a': 1}
        self.assertEqual(get_key(dict), ['a'])

    def test_multiple_key_dict(self):
        dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(get_key(dict), ['a', 'b', 'c', 'd'])

    def test_dict_with_non_string_keys(self):
        dict = {1: 'one', 2: 'two', 3: 'three'}
        self.assertEqual(get_key(dict), [1, 2, 3])

    def test_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            get_key(123)

    def test_dict_with_non_dict_input_type_error(self):
        with self.assertRaises(TypeError):
            get_key("hello")
