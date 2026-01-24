import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_non_empty_dict(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        result = drop_empty(dict1)
        self.assertEqual(result, dict1)

    def test_empty_dict(self):
        dict1 = {}
        result = drop_empty(dict1)
        self.assertEqual(result, {})

    def test_dict_with_none_values(self):
        dict1 = {'a': 1, 'b': None, 'c': 3}
        result = drop_empty(dict1)
        self.assertEqual(result, {'a': 1, 'c': 3})

    def test_dict_with_empty_values(self):
        dict1 = {'a': 1, 'b': '', 'c': 3}
        result = drop_empty(dict1)
        self.assertEqual(result, {'a': 1, 'c': 3})
