import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(get_key({}), [])

    def test_single_key_dict(self):
        self.assertEqual(get_key({'a': 1}), ['a'])

    def test_multiple_key_dict(self):
        self.assertEqual(get_key({'a': 1, 'b': 2, 'c': 3}), ['a', 'b', 'c'])

    def test_dict_with_non_string_keys(self):
        self.assertEqual(get_key({1: 1, 2: 2, 3: 3}), [1, 2, 3])

    def test_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            get_key(123)

    def test_dict_with_non_dict_input_type_error(self):
        with self.assertRaises(TypeError):
            get_key("hello")
