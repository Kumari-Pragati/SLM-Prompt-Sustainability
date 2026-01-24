import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 3), 1)
        self.assertEqual(left_insertion([1, 3, 5, 7], 8), 4)
        self.assertEqual(left_insertion([1, 3, 5, 7], 0), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(left_insertion([], 1), 0)
        self.assertEqual(left_insertion([1, 3, 5, 7], 1), 0)
        self.assertEqual(left_insertion([1, 3, 5, 7], 7), 3)

    def test_corner_cases(self):
        self.assertEqual(left_insertion([1, 3, 5, 7], 2), 1)
        self.assertEqual(left_insertion([1, 3, 5, 7], 4), 2)
        self.assertEqual(left_insertion([1, 3, 5, 7], 6), 2)
        self.assertEqual(left_insertion([1, 3, 5, 7], 5), 2)
