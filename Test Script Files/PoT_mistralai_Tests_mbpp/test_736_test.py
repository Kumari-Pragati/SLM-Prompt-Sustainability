import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(left_insertion([1, 3, 5], 2), 1)
        self.assertEqual(left_insertion([1, 3, 5], 4), 2)
        self.assertEqual(left_insertion([1, 3, 5], 6), 3)
        self.assertEqual(left_insertion([], 0), 0)
        self.assertEqual(left_insertion([1], 1), 0)
        self.assertEqual(left_insertion([1], 2), 1)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(left_insertion([], -1), 0)
        self.assertEqual(left_insertion([-1], -1), 0)
        self.assertEqual(left_insertion([-1], -2), 1)
        self.assertEqual(left_insertion([0, 1, 2], -1), 0)
        self.assertEqual(left_insertion([0, 1, 2], 0), 0)
        self.assertEqual(left_insertion([0, 1, 2], 1), 0)
        self.assertEqual(left_insertion([0, 1, 2], 2), 1)
        self.assertEqual(left_insertion([0, 1, 2], 3), 2)
