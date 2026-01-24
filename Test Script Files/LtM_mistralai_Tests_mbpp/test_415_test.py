import unittest
from mbpp_415_code import max_Product

class TestMaxProduct(unittest.TestCase):

    def test_simple_pair(self):
        self.assertEqual(max_Product([2, 3]), (2, 3))

    def test_simple_negative_pair(self):
        self.assertEqual(max_Product([-2, -3]), (-2, -3))

    def test_simple_zero(self):
        self.assertEqual(max_Product([0, 1]), (1, 0))

    def test_simple_single_element(self):
        self.assertEqual(max_Product([1]), ("No pairs exists",))

    def test_simple_empty(self):
        self.assertEqual(max_Product([]), ("No pairs exists",))

    def test_edge_case_min_positive(self):
        self.assertEqual(max_Product([1, 2]), (2, 1))

    def test_edge_case_min_negative(self):
        self.assertEqual(max_Product([-1, -2]), (-2, -1))

    def test_edge_case_max_positive(self):
        self.assertEqual(max_Product([100, 200]), (200, 100))

    def test_edge_case_max_negative(self):
        self.assertEqual(max_Product([-100, -200]), (-200, -100))

    def test_complex_case_1(self):
        self.assertEqual(max_Product([1, 2, 3, 4, 5]), (5, 1))

    def test_complex_case_2(self):
        self.assertEqual(max_Product([-1, -2, -3, -4, -5]), (-5, -1))

    def test_complex_case_3(self):
        self.assertEqual(max_Product([1, -1, 2, -2, 3, -3]), (3, -3))
