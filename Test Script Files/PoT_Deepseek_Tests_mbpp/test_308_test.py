import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 2), [36, 30])

    def test_edge_case_with_single_number(self):
        self.assertEqual(large_product([1], [2], 1), [2])

    def test_boundary_case_with_empty_lists(self):
        self.assertEqual(large_product([], [], 0), [])

    def test_corner_case_with_negative_numbers(self):
        self.assertEqual(large_product([-1, -2, -3], [-4, -5, -6], 2), [36, 30])

    def test_corner_case_with_large_numbers(self):
        self.assertEqual(large_product([10**6, 2*10**6], [3*10**6, 4*10**6], 2), [4*10**12, 6*10**12])

    def test_invalid_input_N_greater_than_length_of_result(self):
        with self.assertRaises(IndexError):
            large_product([1, 2, 3], [4, 5, 6], 6)
