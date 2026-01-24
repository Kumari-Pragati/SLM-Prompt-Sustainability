import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_Of_product(1), 2)
        self.assertEqual(sum_Of_product(2), 6)
        self.assertEqual(sum_Of_product(3), 20)

    def test_edge_cases(self):
        self.assertEqual(sum_Of_product(0), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum_Of_product(10), 165580)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            sum_Of_product(-1)
