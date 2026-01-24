import unittest
from mbpp_672_code import range
from six.moves import xrange

from six72_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_of_three(5, 3, 1), 5)
        self.assertEqual(max_of_three(-2, -5, -8), -2)
        self.assertEqual(max_of_three(0, 0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(max_of_three(float('inf'), 3, 1), float('inf'))
        self.assertEqual(max_of_three(-float('inf'), 3, 1), -float('inf'))
        self.assertEqual(max_of_three(3, float('inf'), 1), float('inf'))
        self.assertEqual(max_of_three(3, -float('inf'), 1), 3)
        self.assertEqual(max_of_three(3, 3, float('inf')), float('inf'))
        self.assertEqual(max_of_three(3, 3, -float('inf')), 3)

    def test_boundary_cases(self):
        for i in range(-100, 101):
            for j in range(-100, 101):
                for k in range(-100, 101):
                    self.assertEqual(max_of_three(i, j, k), max(i, j, k))

        for i in xrange(-100, 101, 2):
            for j in xrange(-100, 101, 2):
                for k in xrange(-100, 101, 2):
                    self.assertEqual(max_of_three(i, j, k), max(i, j, k))
