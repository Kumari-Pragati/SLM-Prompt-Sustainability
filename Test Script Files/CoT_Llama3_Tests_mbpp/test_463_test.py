import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_positive_array(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 60)

    def test_negative_array(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -60)

    def test_mixed_array(self):
        self.assertEqual(max_subarray_product([1, -2, 3, -4, 5]), 5)

    def test_zero_array(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0, 0]), 0)

    def test_empty_array(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_single_element_array(self):
        self.assertEqual(max_subarray_product([1]), 1)

    def test_array_with_zero(self):
        self.assertEqual(max_subarray_product([1, 0, 2, 3, 4]), 4)

    def test_array_with_negative_and_positive(self):
        self.assertEqual(max_subarray_product([-1, 2, -3, 4, -5]), 4)
