import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):
    def test_typical(self):
        self.assertListEqual(add_str([('a', 'b'), ('c', 'd')], 'e'), ['a', 'b', 'c', 'd', 'e'])
        self.assertListEqual(add_str([('x',), ('y', 'z')], 'w'), ['x', 'y', 'z', 'w'])
        self.assertListEqual(add_str([('A', 'B'), ('C',)], 'D'), ['A', 'B', 'C', 'D'])

    def test_edge_and_boundary(self):
        self.assertListEqual(add_str([], 'K'), [])
        self.assertListEqual(add_str([('a',)], 'K'), [('a',), 'K'])
        self.assertListEqual(add_str([('a', 'b'), ('c', 'd')], ''), [('a', 'b'), ('c', 'd')])
        self.assertListEqual(add_str([('a', 'b')], 'a'), ['a', 'b', 'a'])
        self.assertListEqual(add_str([('a', 'b')], 'aa'), ['a', 'b', 'aa'])
