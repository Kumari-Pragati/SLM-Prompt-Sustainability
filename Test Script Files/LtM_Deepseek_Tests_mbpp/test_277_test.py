import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3}, 2), {'b': 2, 'c': 3})

    def test_edge_condition_empty_dict(self):
        self.assertEqual(dict_filter({}, 2), {})

    def test_edge_condition_all_values_below_n(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 0, 'c': -1}, 2), {})

    def test_boundary_condition_n_equals_min_value(self):
        self.assertEqual(dict_filter({'a': -1, 'b': 0, 'c': 1}, -1), {'a': -1, 'b': 0, 'c': 1})

    def test_boundary_condition_n_equals_max_value(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3}, 3), {'c': 3})

    def test_complex_input(self):
        self.assertEqual(dict_filter({'a': 2, 'b': 3, 'c': 4, 'd': 5}, 3), {'b': 3, 'c': 4, 'd': 5})
