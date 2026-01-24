import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), 120)
        self.assertEqual(max_product([0, 0, 0, 0, 0], 5), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_product([1], 1), 1)
        self.assertEqual(max_product([1, 2], 2), 2)
        self.assertEqual(max_product([1, 2, 3], 3), 6)
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), 120)
        self.assertEqual(max_product([0, 0, 0, 0, 0], 5), 0)
        self.assertEqual(max_product([1, 2, 3, 4, 5, 6], 6), 720)
        self.assertEqual(max_product([-1, -2, -3, -4, -5, -6], 6), 720)
        self.assertEqual(max_product([0, 0, 0, 0, 0, 0], 6), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, 3], 3), 18)
        self.assertEqual(max_product([-1, 2, -3, 4], 4), 24)
        self.assertEqual(max_product([-1, 2, -3, 4, -5], 5), 12)
        self.assertEqual(max_product([-1, 2, -3, 4, -5, -6], 6), 72)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            max_product([], 0)
        with self.assertRaises(ValueError):
            max_product([1], -1)
