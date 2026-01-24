import unittest
from mbpp_592_code import sum_Of_product

class TestSumOfProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_product(1), 1)

    def test_edge_case(self):
        self.assertEqual(sum_Of_product(2), 2)

    def test_edge_case2(self):
        self.assertEqual(sum_Ofproduct(3), 4)

    def test_edge_case3(self):
        self.assertEqual(sum_Ofproduct(4), 6)

    def test_edge_case4(self):
        self.assertEqual(sum_Ofproduct(5), 8)

    def test_edge_case5(self):
        self.assertEqual(sum_Ofproduct(6), 12)
