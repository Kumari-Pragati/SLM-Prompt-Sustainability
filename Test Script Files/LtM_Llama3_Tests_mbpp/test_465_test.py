import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_simple_valid_input(self):
        dict1 = {'a': 1, 'b': 2, 'c': None}
        result = drop_empty(dict1)
        self.assertEqual(result, {'a': 1, 'b': 2})

    def test_empty_input(self):
        dict1 = {}
        result = drop_empty(dict1)
        self.assertEqual(result, {})

    def test_all_none_values(self):
        dict1 = {'a': None, 'b': None, 'c': None}
        result = drop_empty(dict1)
        self.assertEqual(result, {})

    def test_mixed_values(self):
        dict1 = {'a': 1, 'b': None, 'c': 3, 'd': None}
        result = drop_empty(dict1)
        self.assertEqual(result, {'a': 1, 'c': 3})

    def test_dict_with_single_none_value(self):
        dict1 = {'a': 1, 'b': None, 'c': 3}
        result = drop_empty(dict1)
        self.assertEqual(result, {'a': 1, 'c': 3})
