import unittest
from mbpp_513_code import add_str

class TestAddStr(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add_str([('a',), ('b',), ('c',)], 'd'), ['a', 'b', 'c', 'd'])
        self.assertEqual(add_str([('x', 'y'), ('z',)], 'w'), ['x', 'y', 'z', 'w'])

    def test_edge_cases(self):
        self.assertEqual(add_str([], 'K'), [])
        self.assertEqual(add_str([('K',)], ''), ['K'])
        self.assertEqual(add_str([('a',), ('K',)], ('b',)), ['a', 'K', 'b'])

    def test_complex(self):
        self.assertEqual(add_str([('a',), ('b',), ('c',), ('d',)], 'e'), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(add_str([('x', 'y'), ('z', 'w')], 'v'), ['x', 'y', 'z', 'w', 'v'])
        self.assertEqual(add_str([('a',), ('b',), ('c',), ('d',), ('e',)], ('f', 'g')), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
