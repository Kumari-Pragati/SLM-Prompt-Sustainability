import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None}), {'a': 1})

    def test_empty_input(self):
        self.assertEqual(drop_empty({}), {})

    def test_edge_case_with_all_none_values(self):
        self.assertEqual(drop_empty({'a': None, 'b': None, 'c': None}), {})

    def test_complex_input(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 2, 'd': None}), {'a': 1, 'c': 2})
