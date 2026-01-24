import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 6)

    def test_edge_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6]), 6)

    def test_edge_case_negative(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -6)

    def test_edge_case_single_element(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            maximum_product([])

    def test_edge_case_single_element_negative(self):
        self.assertEqual(maximum_product([-1]), -1)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(maximum_product([0]), 0)

    def test_edge_case_single_element_positive(self):
        self.assertEqual(maximum_product([1]), 1)

    def test_edge_case_multiple_elements(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]), 6)

    def test_edge_case_multiple_elements_negative(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6, -7, -8, -9]), -6)

    def test_edge_case_multiple_elements_positive(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]), 6)

    def test_edge_case_multiple_elements_zero(self):
        self.assertEqual(maximum_product([0, 0, 0, 0, 0, 0, 0, 0, 0]), 0)

    def test_edge_case_multiple_elements_zero_and_positive(self):
        self.assertEqual(maximum_product([0, 1, 2, 3, 4, 5, 6, 7, 8]), 6)

    def test_edge_case_multiple_elements_zero_and_negative(self):
        self.assertEqual(maximum_product([0, -1, -2, -3, -4, -5, -6, -7, -8]), -6)

    def test_edge_case_multiple_elements_zero_and_positive(self):
        self.assertEqual(maximum_product([0, 1, 2, 3, 4, 5, 6, 7, 8]), 6)
