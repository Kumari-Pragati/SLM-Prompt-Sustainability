import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(largest_neg([-100, -200, -300]), -300)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(largest_neg([]), None)
        self.assertEqual(largest_neg([0]), 0)
        self.assertEqual(largest_neg([-1]), -1)
        self.assertEqual(largest_neg([-1, 0]), -1)
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5, -6]), -6)

    def test_negative_numbers_only(self):
        self.assertEqual(largest_neg([-1, 0, -2]), -2)
        self.assertEqual(largest_neg([-100, 0, -200]), -200)

    def test_mixed_numbers(self):
        self.assertEqual(largest_neg([-1, 2, -3, 4, -5]), -5)
        self.assertEqual(largest_neg([100, -200, 300]), -200)
