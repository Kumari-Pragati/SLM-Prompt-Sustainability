import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(largest_neg([-1, -2, -3]), -1)

    def test_edge_boundary_conditions(self):
        self.assertEqual(largest_neg([0]), 0)
        self.assertEqual(largest_neg([-1]), -1)
        self.assertEqual(largest_neg([1]), 1)
        self.assertEqual(largest_neg([-1, 0, 1]), 0)

    def test_complex_cases(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4]), -1)
        self.assertEqual(largest_neg([1, 2, 3, 4]), 1)
        self.assertEqual(largest_neg([0, -1, 1]), 0)
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(largest_neg([1, 2, 3, 4, 5]), 1)

    def test_empty_input(self):
        self.assertIsNone(largest_neg([]))
