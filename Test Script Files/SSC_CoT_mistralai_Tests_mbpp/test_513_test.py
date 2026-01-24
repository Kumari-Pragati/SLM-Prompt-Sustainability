import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(add_str([('a', 'b'), ('c', 'd')], 'e'), ['a', 'b', 'c', 'd', 'e'])
        self.assertListEqual(add_str([('A', 'B'), ('C', 'D')], 'E'), ['A', 'B', 'C', 'D', 'E'])

    def test_edge_input(self):
        self.assertListEqual(add_str([], 'e'), ['e'])
        self.assertListEqual(add_str([('a',)], 'e'), ['a', 'e'])
        self.assertListEqual(add_str([('a', 'b'), ('c',)], 'd'), ['a', 'b', 'c', 'd'])
        self.assertListEqual(add_str([('a', 'b')], ''), ['a', 'b'])

    def test_boundary_input(self):
        self.assertListEqual(add_str([('a', 'b') for _ in range(1000)], 'c'), list(range(1000)) + ['c'])
        self.assertListEqual(add_str([('a', 'b') for _ in range(1000)], ''), list(range(1000)))

    def test_invalid_input(self):
        self.assertRaises(TypeError, add_str, [1, 2], 'e')
        self.assertRaises(TypeError, add_str, [('a', 'b'), 1], 'e')
