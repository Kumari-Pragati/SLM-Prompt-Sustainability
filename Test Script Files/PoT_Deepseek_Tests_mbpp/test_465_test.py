import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(drop_empty({'a': 1, 'b': None, 'c': 'test'}), {'a': 1, 'c': 'test'})

    def test_edge_case_empty_dict(self):
        self.assertEqual(drop_empty({}), {})

    def test_boundary_case_all_values_none(self):
        self.assertEqual(drop_empty({'a': None, 'b': None, 'c': None}), {})

    def test_corner_case_all_values_are_not_none(self):
        self.assertEqual(drop_empty({'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    def test_tricky_case_mixed_values(self):
        self.assertEqual(drop_empty({'a': None, 'b': 2, 'c': None}), {'b': 2})
