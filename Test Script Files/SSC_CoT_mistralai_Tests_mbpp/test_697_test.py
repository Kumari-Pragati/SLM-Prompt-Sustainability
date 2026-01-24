import unittest
from mbpp_697_code import filter
from six.moves import range

from697_code import count_even

class TestCountEven(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_even([0, 2, 4, 6]), 4)
        self.assertEqual(count_even([-2, -4, -6]), 3)
        self.assertEqual(count_even([1, 3, 5, 7]), 0)

    def test_edge_input(self):
        self.assertEqual(count_even([]), 0)
        self.assertEqual(count_even([0]), 1)
        self.assertEqual(count_even([1, 2, 3]), 1)
        self.assertEqual(count_even([0, 2, 4, 6, 8]), 5)

    def test_boundary_input(self):
        self.assertEqual(count_even([-1, 0, 1]), 1)
        self.assertEqual(count_even([-2, -1, 0, 1, 2]), 3)
        self.assertEqual(count_even([-2, -1, 0, 1, 2, 3]), 1)
        self.assertEqual(count_even([-2, -1, 0, 1, 2, 3, 4]), 3)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_even, 'not a list')
        self.assertRaises(TypeError, count_even, [1.23])
