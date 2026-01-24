import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 5))

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([1]), (None,))

    def test_edge_case_two_elements(self):
        self.assertEqual(max_product([1, 2]), (1, 2))

    def test_edge_case_three_elements(self):
        self.assertEqual(max_product([1, 2, 3]), (1, 3))

    def test_edge_case_all_equal(self):
        self.assertEqual(max_product([1, 1, 1, 1]), (1, 1))

    def test_edge_case_all_negative(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))

    def test_edge_case_all_positive(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (1, 4))

    def test_edge_case_all_zero(self):
        self.assertEqual(max_product([0, 0, 0, 0]), (None,))

    def test_edge_case_mixed_signs(self):
        self.assertEqual(max_product([-1, 2, -3, 4]), (-1, 4))

    def test_edge_case_mixed_zero(self):
        self.assertEqual(max_product([0, 1, 2, 3]), (1, 3))

    def test_edge_case_mixed_negative(self):
        self.assertEqual(max_product([-1, -2, -3, -4]), (-1, -2))

    def test_edge_case_mixed_positive(self):
        self.assertEqual(max_product([1, 2, 3, 4]), (1, 4))
