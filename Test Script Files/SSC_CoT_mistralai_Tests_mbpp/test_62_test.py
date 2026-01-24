import unittest
from mbpp_62_code import range
from six.moves import xrange

from62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(smallest_num([1, 2, 3, 4]), 1)
        self.assertEqual(smallest_num((1, 2, 3, 4)), 1)
        self.assertEqual(smallest_num([4, 3, 2, 1]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4]), -4)
        self.assertEqual(smallest_num([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(smallest_num([]), None)
        self.assertEqual(smallest_num([None]), None)
        self.assertEqual(smallest_num([float('nan')]), float('nan'))
        self.assertEqual(smallest_num([float('inf')]), float('inf'))
        self.assertEqual(smallest_num([-float('inf')]), -float('inf'))

    def test_boundary_cases(self):
        self.assertEqual(smallest_num(range(-100, 101)), -100)
        self.assertEqual(smallest_num(xrange(-100, 101)), -100)
        self.assertEqual(smallest_num(range(0, 101)), 0)
        self.assertEqual(smallest_num(xrange(0, 101)), 0)
        self.assertEqual(smallest_num(range(-100, 0)), -100)
        self.assertEqual(smallest_num(xrange(-100, 0)), -100)
