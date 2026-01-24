import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(drop_empty({}), {})

    def test_dict_with_empty_values(self):
        self.assertEqual(drop_empty({'a': None, 'b': '', 'c': 0}), {'c': 0})

    def test_dict_with_non_empty_values(self):
        self.assertEqual(drop_empty({'a': 'hello', 'b': 123, 'c': None}), {'a': 'hello', 'b': 123})

    def test_dict_with_mixed_values(self):
        self.assertEqual(drop_empty({'a': 'hello', 'b': None, 'c': 123, 'd': ''}), {'a': 'hello', 'c': 123})

    def test_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            drop_empty('not a dict')

    def test_dict_with_non_dict_input_type_error(self):
        with self.assertRaises(TypeError):
            drop_empty([1, 2, 3])
