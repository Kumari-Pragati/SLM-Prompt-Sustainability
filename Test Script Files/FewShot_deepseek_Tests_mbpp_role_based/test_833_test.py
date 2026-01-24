import unittest
from mbpp_833_code import get_key

class TestGetKey(unittest.TestCase):
    def test_typical_use_case(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(get_key(test_dict), ['a', 'b', 'c'])

    def test_empty_dictionary(self):
        test_dict = {}
        self.assertEqual(get_key(test_dict), [])

    def test_dictionary_with_duplicates(self):
        test_dict = {'a': 1, 'b': 2, 'a': 3}
        self.assertEqual(get_key(test_dict), ['a', 'b'])

    def test_dictionary_with_integer_keys(self):
        test_dict = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(get_key(test_dict), [1, 2, 3])

    def test_dictionary_with_mixed_keys(self):
        test_dict = {'a': 1, 2: 'b', 3: 'c'}
        self.assertEqual(get_key(test_dict), ['a', 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_key(123)
