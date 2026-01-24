import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(drop_empty({}), {})

    def test_non_empty_dict(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 3}), {'a': 1, 'c': 3})

    def test_dict_with_all_none_values(self):
        self.assertEqual(drop_empty({'a': None, 'b': None, 'c': None}), {})

    def test_dict_with_no_none_values(self):
        self.assertEqual(drop_empty({'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    def test_dict_with_mixed_values(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 3, 'd': None, 'e': 5}), {'a': 1, 'c': 3, 'e': 5})
