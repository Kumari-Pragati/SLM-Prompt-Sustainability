import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_Of_product(1), 1)
        self.assertEqual(sum_Of_product(2), 2)
        self.assertEqual(sum_Of_product(3), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Of_product(0), 0)
        self.assertEqual(sum_Of_product(1000), 1977121875200)
        self.assertEqual(sum_Of_product(-1), None)
        self.assertEqual(sum_Of_product(1.5), None)
