import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_drop_empty(self):
        self.assertEqual(drop_empty({}), {})
        self.assertEqual(drop_empty({'a': None}), {})
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 3}), {'a': 1, 'c': 3})
        self.assertEqual(drop_empty({'a': None, 'b': None, 'c': None}), {})
        self.assertEqual(drop_empty({'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(drop_empty({'a': None, 'b': 2, 'c': None, 'd': 4}), {'b': 2, 'd': 4})

    def test_drop_empty_with_empty_list(self):
        self.assertEqual(drop_empty({}), {})
        self.assertEqual(drop_empty({'a': None}), {})
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 3}), {'a': 1, 'c': 3})
        self.assertEqual(drop_empty({'a': None, 'b': None, 'c': None}), {})
        self.assertEqual(drop_empty({'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(drop_empty({'a': None, 'b': 2, 'c': None, 'd': 4}), {'b': 2, 'd': 4})
