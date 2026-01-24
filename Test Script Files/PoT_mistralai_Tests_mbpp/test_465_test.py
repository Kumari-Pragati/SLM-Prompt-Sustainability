import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):
    def test_typical_case(self):
        self.assertDictEqual(drop_empty({'a': 1, 'b': None, 'c': 3}), {'a': 1, 'c': 3})

    def test_edge_case_empty_dict(self):
        self.assertDictEqual(drop_empty({}), {})

    def test_edge_case_single_key(self):
        self.assertDictEqual(drop_empty({'a': None}), {})

    def test_edge_case_single_value(self):
        self.assertDictEqual(drop_empty({None: 'x'}), {})

    def test_corner_case_mixed_values(self):
        self.assertDictEqual(drop_empty({'a': 1, 'b': 'two', 'c': None}), {'a': 1, 'b': 'two'})
