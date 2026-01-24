import unittest
from mbpp_277_code import dict_filter

class TestDictFilter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 3}, 2), {'b': 2, 'c': 3})

    def test_edge_case(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 2}, 2), {'b': 2, 'c': 2})

    def test_boundary_case(self):
        self.assertEqual(dict_filter({'a': 1, 'b': 2, 'c': 1}, 1), {'b': 2})

    def test_corner_case(self):
        self.assertEqual(dict_filter({'a': 0, 'b': -1, 'c': 0}, 0), {'a': 0, 'c': 0})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dict_filter(123, 2)
