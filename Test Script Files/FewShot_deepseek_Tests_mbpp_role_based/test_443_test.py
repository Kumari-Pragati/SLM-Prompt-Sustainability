import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4]), -1)

    def test_edge_condition(self):
        self.assertEqual(largest_neg([0]), 0)

    def test_boundary_condition(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4, 0]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            largest_neg("not a list")

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            largest_neg([])
