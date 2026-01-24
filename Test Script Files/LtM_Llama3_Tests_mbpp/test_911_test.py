import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 6)

    def test_edge_case_empty_input(self):
        self.assertRaises(ValueError, maximum_product, [])

    def test_edge_case_single_element_input(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_edge_case_two_element_input(self):
        self.assertEqual(maximum_product([1, 2]), 2)

    def test_edge_case_three_element_input(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)

    def test_edge_case_max_and_min_values(self):
        self.assertEqual(maximum_product([-1, -2, 3, 4, 5]), 60)

    def test_edge_case_max_and_min_values_negative(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -30)

    def test_edge_case_max_and_min_values_zero(self):
        self.assertEqual(maximum_product([0, 0, 0, 0, 0]), 0)

    def test_edge_case_max_and_min_values_all_zero(self):
        self.assertEqual(maximum_product([0, 0, 0]), 0)

    def test_edge_case_max_and_min_values_all_negative(self):
        self.assertEqual(maximum_product([-1, -2, -3]), -6)

    def test_edge_case_max_and_min_values_all_positive(self):
        self.assertEqual(maximum_product([1, 2, 3]), 6)

    def test_edge_case_max_and_min_values_mixed(self):
        self.assertEqual(maximum_product([-1, 0, 1]), 0)

    def test_edge_case_max_and_min_values_mixed_negative(self):
        self.assertEqual(maximum_product([-1, 0, 1]), 0)
