import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_single_element(self):
        for num in [-1, 0, 1]:
            self.assertEqual(max_subarray_product([num]), num)

    def test_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -24)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([1, -2, 3, -4, 5]), 15)

    def test_zero_in_middle(self):
        self.assertEqual(max_subarray_product([1, 0, 2, -1]), 2)

    def test_zero_at_start(self):
        self.assertEqual(max_subarray_product([0, 1, 2, 3]), 6)

    def test_zero_at_end(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 0]), 6)

    def test_all_zeros(self):
        self.assertEqual(max_subarray_product([0, 0, 0]), 0)

    def test_negative_numbers_with_zero(self):
        self.assertEqual(max_subarray_product([-1, 0, -2]), -2)
