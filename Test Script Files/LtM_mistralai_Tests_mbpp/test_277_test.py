import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(dict_filter({'a': 1, 'b': 2, 'c': 3}, 2), {'b': 2, 'c': 3})
        self.assertDictEqual(dict_filter({'a': 5, 'b': 2, 'c': -1}, 2), {'a': 5})
        self.assertDictEqual(dict_filter({'a': 0, 'b': 2, 'c': -1}, 1), {'a': 0})

    def test_edge_cases(self):
        self.assertDictEqual(dict_filter({}, 1), {})
        self.assertDictEqual(dict_filter({'a': 0}, 1), {'a': 0})
        self.assertDictEqual(dict_filter({'a': float('inf')}, 100), {'a': float('inf')})

    def test_complex(self):
        self.assertDictEqual(dict_filter({'a': -1, 'b': 0, 'c': 1, 'd': -100}, 0), {'b': 0})
        self.assertDictEqual(dict_filter({'a': 1.0000001, 'b': 2, 'c': 3}, 2), {'b': 2, 'c': 3})
        self.assertDictEqual(dict_filter({'a': -1, 'b': -2, 'c': -3}, -4), {'a': -1, 'b': -2, 'c': -3})
