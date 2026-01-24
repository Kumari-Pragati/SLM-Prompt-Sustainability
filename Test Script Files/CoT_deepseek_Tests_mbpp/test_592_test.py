import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_product(3), 10)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Of_product(0), 1)
        self.assertEqual(sum_Of_product(1), 2)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_product(2), 6)
        self.assertEqual(sum_Of_product(5), 210)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            sum_Of_product(-1)
        with self.assertRaises(Exception):
            sum_Of_product(1.5)
        with self.assertRaises(Exception):
            sum_Of_product('a')
