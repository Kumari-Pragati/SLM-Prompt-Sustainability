import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 3}), {'a': 1, 'c': 3})

    def test_edge_case_empty_input(self):
        self.assertEqual(drop_empty({}), {})

    def test_edge_case_all_none_values(self):
        self.assertEqual(drop_empty({'a': None, 'b': None, 'c': None}), {})

    def test_edge_case_all_non_none_values(self):
        self.assertEqual(drop_empty({'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    def test_edge_case_mixed_values(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 3, 'd': None}), {'a': 1, 'c': 3})

    def test_edge_case_dict_with_single_none_value(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 3}), {'a': 1, 'c': 3})

    def test_edge_case_dict_with_multiple_none_values(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': None, 'd': None}), {'a': 1})

    def test_edge_case_dict_with_all_none_values(self):
        self.assertEqual(drop_empty({'a': None, 'b': None, 'c': None, 'd': None}), {})
