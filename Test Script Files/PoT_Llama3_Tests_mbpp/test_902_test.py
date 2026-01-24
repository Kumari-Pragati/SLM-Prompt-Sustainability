import unittest
from mbpp_902_code import add_dict

class TestAddDict(unittest.TestCase):
    def test_typical_case(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        self.assertEqual(add_dict(d1, d2), Counter({'a': 1, 'b': 5, 'c': 4}))

    def test_edge_case_empty_dict(self):
        d1 = {}
        d2 = {'a': 1, 'b': 2}
        self.assertEqual(add_dict(d1, d2), Counter({'a': 1, 'b': 2}))

    def test_edge_case_single_dict(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}
        self.assertEqual(add_dict(d1, d2), Counter({'a': 1, 'b': 2}))

    def test_edge_case_equal_dicts(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 2}
        self.assertEqual(add_dict(d1, d2), Counter({'a': 1, 'b': 2}))

    def test_edge_case_dict_with_duplicates(self):
        d1 = {'a': 1, 'b': 2, 'b': 3}
        d2 = {'b': 4, 'c': 5}
        self.assertEqual(add_dict(d1, d2), Counter({'a': 1, 'b': 7, 'c': 5}))

    def test_edge_case_dict_with_negative_values(self):
        d1 = {'a': -1, 'b': 2}
        d2 = {'b': -3, 'c': 4}
        self.assertEqual(add_dict(d1, d2), Counter({'a': -1, 'b': -1, 'c': 4}))
