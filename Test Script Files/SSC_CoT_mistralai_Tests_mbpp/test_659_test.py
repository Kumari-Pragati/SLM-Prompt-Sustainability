import unittest
from mbpp_659_code import range
from six.moves import zip_longest
from six.moves import xrange

from 659_code import Repeat

class TestRepeat(unittest.TestCase):

    def test_typical_input(self):
        self.assertListEqual(Repeat('abcd'), ['a', 'c'])
        self.assertListEqual(Repeat('abcdefg'), ['a', 'c', 'e'])
        self.assertListEqual(Repeat('a'), ['a'])
        self.assertListEqual(Repeat(''), [])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(Repeat('aabb'), ['a', 'b'])
        self.assertListEqual(Repeat('aabba'), ['a', 'b'])
        self.assertListEqual(Repeat('aaa'), ['a'])
        self.assertListEqual(Repeat('abab'), [])
        self.assertListEqual(Repeat('a' * 10000), ['a'])

    def test_special_cases(self):
        self.assertListEqual(Repeat('123123'), [1, 3])
        self.assertListEqual(Repeat('abc123abc'), ['a', 'c'])
        self.assertListEqual(Repeat('123456789'), [1, 5, 9])
        self.assertListEqual(Repeat('1234567890'), [1, 5, 9])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, Repeat, 123)
        self.assertRaises(TypeError, Repeat, (1, 2, 3))
        self.assertRaises(TypeError, Repeat, [1, 2, 3, 4])
        self.assertRaises(TypeError, Repeat, {'a': 1, 'b': 2})
