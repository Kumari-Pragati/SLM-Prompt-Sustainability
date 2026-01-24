import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 2)
        self.assertEqual(sum_Of_product(3), 5)
        self.assertEqual(sum_Of_product(4), 14)
        self.assertEqual(sum_Of_product(5), 35)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(sum_Of_product(0), 0)
        self.assertEqual(sum_Of_product(100), 17710)
        self.assertEqual(sum_Of_product(-1), None)
