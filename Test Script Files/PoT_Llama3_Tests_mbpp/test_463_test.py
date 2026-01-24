import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_subarray_product([2, 3, -2, 4]), 6)

    def test_edge_case_zero(self):
        self.assertEqual(max_subarray_product([0, 1, 2]), 2)

    def test_edge_case_negative(self):
        self.assertEqual(max_subarray_product([-1, -2, -3]), -6)

    def test_edge_case_positive(self):
        self.assertEqual(max_subarray_product([1, 2, 3]), 6)

    def test_edge_case_zero_array(self):
        self.assertEqual(max_subarray_product([0]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_subarray_product([1]), 1)

    def test_edge_case_empty_array(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_edge_case_all_negative(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -12)

    def test_edge_case_all_positive(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)

    def test_edge_case_mixed(self):
        self.assertEqual(max_subarray_product([-1, 2, -3, 4]), 4)
