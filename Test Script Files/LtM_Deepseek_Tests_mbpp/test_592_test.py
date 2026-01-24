import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_Of_product(1), 2)
        self.assertEqual(sum_Of_product(2), 6)
        self.assertEqual(sum_Of_product(3), 20)

    def test_edge_conditions(self):
        self.assertEqual(sum_Of_product(0), 1)
        self.assertEqual(sum_Of_product(1), 2)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Of_product(10), 165580140)
        self.assertEqual(sum_Of_product(20), 184756062222298138908919182050)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            sum_Of_product(-1)
        with self.assertRaises(Exception):
            sum_Of_product(1.5)
        with self.assertRaises(Exception):
            sum_Of_product('a')
