import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(left_insertion([1, 3, 5], 2), 1)
        self.assertEqual(left_insertion([1, 3, 5], 4), 2)
        self.assertEqual(left_insertion([1, 3, 5], 6), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(left_insertion([], 1), 0)
        self.assertEqual(left_insertion([1], 1), 0)
        self.assertEqual(left_insertion([1], 2), 1)
        self.assertEqual(left_insertion([1, 1], 1), 0)
        self.assertEqual(left_insertion([1, 1], 2), 1)
        self.assertEqual(left_insertion([1, 1, 1], 1), 0)
        self.assertEqual(left_insertion([1, 1, 1], 2), 1)
        self.assertEqual(left_insertion([1, 1, 1], 3), 2)
        self.assertEqual(left_insertion([1, 1, 1], float('inf')), 3)

    def test_complex(self):
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 0), 0)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], -6), 0)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], -4), 1)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], -3), 2)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], -2), 3)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], -1), 4)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 0), 5)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 1), 5)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 2), 5)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 3), 5)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 4), 5)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 5), 5)
        self.assertEqual(left_insertion([-5, -3, -1, 1, 3, 5], 6), 6)
