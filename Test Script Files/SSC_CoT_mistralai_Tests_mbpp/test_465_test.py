import unittest
from mbpp_465_code import drop_empty

class TestDropEmpty(unittest.TestCase):

    def test_normal_input(self):
        self.assertDictEqual(drop_empty({1: 'a', 2: None, 3: 'b'}), {1: 'a', 3: 'b'})
        self.assertDictEqual(drop_empty({'a': 1, 'b': None, 'c': 2}), {'a': 1, 'c': 2})

    def test_edge_and_boundary_conditions(self):
        self.assertDictEqual(drop_empty({None: 'a'}), {})
        self.assertDictEqual(drop_empty({'a': None, 'b': None}), {})
        self.assertDictEqual(drop_empty({'a': '', 'b': None}), {'a': ''})
        self.assertDictEqual(drop_empty({'a': 0, 'b': None}), {'a': 0})
        self.assertDictEqual(drop_empty({None: None}), {})

    def test_special_cases(self):
        self.assertDictEqual(drop_empty({None: (1, 2, 3)}), {})
        self.assertDictEqual(drop_empty({'a': [None], 'b': [1, 2, None]}), {'b': [1, 2]})
