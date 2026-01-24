import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 5))

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([1]), (None,))

    def test_edge_case_two_elements(self):
        self.assertEqual(max_product([1, 2]), (1, 2))

    def test_edge_case_two_elements_equal(self):
        self.assertEqual(max_product([2, 2]), (2, 2))

    def test_edge_case_empty_list(self):
        self.assertEqual(max_product([]), (None,))

    def test_edge_case_single_element_zero(self):
        self.assertEqual(max_product([0]), (None,))

    def test_edge_case_two_elements_zero(self):
        self.assertEqual(max_product([0, 1]), (0, 1))

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, 3]), (-1, 3))

    def test_edge_case_positive_and_negative_numbers(self):
        self.assertEqual(max_product([1, -2, 3]), (1, 3))

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3]), (-1, -3))

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 3))

    def test_edge_case_max_product_is_zero(self):
        self.assertEqual(max_product([0, 0, 1]), (0, 1))

    def test_edge_case_max_product_is_negative(self):
        self.assertEqual(max_product([-1, -2, -3]), (-1, -3))

    def test_edge_case_max_product_is_positive(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 3))

    def test_edge_case_max_product_is_positive_and_negative(self):
        self.assertEqual(max_product([1, -2, 3]), (1, 3))

    def test_edge_case_max_product_is_negative_and_positive(self):
        self.assertEqual(max_product([-1, 2, 3]), (-1, 3))
