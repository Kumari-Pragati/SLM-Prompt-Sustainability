import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(unique_product([1, 2, 3, 4]), 24)
        self.assertEqual(unique_product([5, 5, 5, 5]), 625)

    def test_edge_conditions(self):
        self.assertEqual(unique_product([]), 1)
        self.assertEqual(unique_product([0]), 0)
        self.assertEqual(unique_product([1]), 1)

    def test_boundary_conditions(self):
        self.assertEqual(unique_product([-1, -2, -3, -4]), -24)
        self.assertEqual(unique_product([-1, -1, -1, -1]), 1)

    def test_complex_cases(self):
        self.assertEqual(unique_product([1, 2, 3, 4, 0]), 0)
        self.assertEqual(unique_product([-1, -2, -3, -4, 0]), 0)
        self.assertEqual(unique_product([1, 2, 3, 4, -1]), -24)
