import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(new_tuple([1, 2, 3], 'a'), ([1, 2, 3, 'a']))
        self.assertEqual(new_tuple([], 'b'), ('', 'b'))
        self.assertEqual(new_tuple(['x'], 'y'), ('x', 'y'))

    def test_edge_cases(self):
        self.assertEqual(new_tuple([0], 'z'), ([0, 'z']))
        self.assertEqual(new_tuple(['a', 'b', 'c'], 'd'), (['a', 'b', 'c', 'd']))
        self.assertEqual(new_tuple([999999], 'z'), ([999999, 'z']))

    def test_complex(self):
        self.assertEqual(new_tuple([1, 2, 3, 4, 5], 'f'), ([1, 2, 3, 4, 5, 'f']))
        self.assertEqual(new_tuple([], 'x'), ('x',))
        self.assertEqual(new_tuple(['a', 'b', 'c', 'd'], 'e'), (['a', 'b', 'c', 'd', 'e']))
