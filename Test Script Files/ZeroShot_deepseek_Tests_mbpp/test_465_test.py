import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_drop_empty_with_empty_dict(self):
        self.assertEqual(drop_empty({}), {})

    def test_drop_empty_with_dict_with_none_values(self):
        self.assertEqual(drop_empty({'a': None, 'b': None}), {})

    def test_drop_empty_with_dict_with_some_none_values(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 2}), {'a': 1, 'c': 2})

    def test_drop_empty_with_dict_with_all_values(self):
        self.assertEqual(drop_empty({'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})
