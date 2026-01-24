import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_typical_input(self):
        data = {'a': 10, 'b': 20, 'c': 5, 'd': 15}
        result = dict_filter(data, 10)
        self.assertDictEqual(result, {'a': 10, 'b': 20})

    def test_edge_cases(self):
        data = {'a': 0, 'b': 1, 'c': -1, 'd': 2147483647}
        result = dict_filter(data, 0)
        self.assertDictEqual(result, {'b': 1})
        result = dict_filter(data, -1)
        self.assertDictEqual(result, {'c': -1})
        result = dict_filter(data, 2147483647)
        self.assertDictEqual(result, {'d': 2147483647})

    def test_boundary_cases(self):
        data = {'a': float('inf'), 'b': -float('inf'), 'c': 0, 'd': 1}
        result = dict_filter(data, 0)
        self.assertDictEqual(result, {'c': 0})
        result = dict_filter(data, -float('inf'))
        self.assertDictEqual(result, {'b': -float('inf')})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dict_filter(123, 456)
        with self.assertRaises(TypeError):
            dict_filter({'a': 1}, '2')
