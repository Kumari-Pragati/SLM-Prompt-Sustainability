import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (3, 4))
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))
        self.assertEqual(max_product([0, 1, 2, 3]), (0, 3))

    def test_edge_and_boundary_conditions(self):
        self.assertIsNone(max_product([]))
        self.assertIsNone(max_product([1]))
        self.assertEqual(max_product([0, 0]), (0, 0))
        self.assertEqual(max_product([-1, -1]), (-1, -1))

    def test_more_complex_or_corner_cases(self):
        self.assertEqual(max_product([-1, -2, 3, 4]), (3, 4))
        self.assertEqual(max_product([1, 2, -3, -4]), (1, 2))
        self.assertEqual(max_product([0, -1, -2, 3]), (0, 3))
        self.assertEqual(max_product([-1, -2, -3, 0]), (0, -1))
