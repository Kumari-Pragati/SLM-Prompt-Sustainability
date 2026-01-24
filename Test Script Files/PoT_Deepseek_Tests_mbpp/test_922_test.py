import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (3, 4))

    def test_edge_case_single_element(self):
        self.assertIsNone(max_product([1]))

    def test_edge_case_two_elements(self):
        self.assertEqual(max_product([1, 2]), (1, 2))

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))

    def test_boundary_case_positive_and_negative_numbers(self):
        self.assertEqual(max_product([-1, 2, 3, 4]), (4, 3))

    def test_corner_case_all_positive(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (3, 4))

    def test_corner_case_all_negative(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))

    def test_corner_case_duplicates(self):
        self.assertEqual(max_product([1, 2, 2, 4]), (2, 4))

    def test_corner_case_max_product_is_zero(self):
        self.assertEqual(max_product([0, 0, 0, 0]), (0, 0))
