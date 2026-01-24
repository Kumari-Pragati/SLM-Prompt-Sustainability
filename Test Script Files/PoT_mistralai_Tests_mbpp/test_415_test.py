import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_Product([1, 2, 3, 4]), (1, 4))
        self.assertEqual(max_Product([-1, -2, -3, -4]), (-1, -4))
        self.assertEqual(max_Product([0, 1, 2, 3]), (0, 3))

    def test_edge_case_single_element(self):
        self.assertEqual(max_Product([1]), ("No pairs exists",))

    def test_edge_case_two_elements(self):
        self.assertEqual(max_Product([1, 2]), (1, 2))

    def test_corner_case_all_negative(self):
        self.assertEqual(max_Product([-1, -2, -3]), (-1, -3))

    def test_corner_case_all_positive(self):
        self.assertEqual(max_Product([1, 2, 3]), (1, 3))

    def test_corner_case_all_zero(self):
        self.assertEqual(max_Product([0, 0]), ("No pairs exists",))
