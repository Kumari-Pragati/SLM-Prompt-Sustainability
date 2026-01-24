import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 15, 18])

    def test_edge_case_N_zero(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 0), [])

    def test_edge_case_N_equal_to_length(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 6), [18, 15, 12, 12, 15, 18])

    def test_edge_case_N_greater_than_length(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 10), [18, 15, 12, 12, 15, 18, 12, 15, 18, 12])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            large_product([1, 2, 3], 'abc', 3)

    def test_invalid_input_length(self):
        with self.assertRaises(IndexError):
            large_product([1, 2], [3, 4, 5, 6], 3)
