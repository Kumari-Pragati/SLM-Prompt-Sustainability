import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_Of_product(3), 15)

    def test_boundary_condition(self):
        self.assertEqual(sum_Of_product(0), 1)

    def test_edge_condition(self):
        self.assertEqual(sum_Of_product(1), 2)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            sum_Of_product(-1)
