import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -1)
        self.assertEqual(max_subarray_product([-2, -3, 7, -15, 7]), 105)
        self.assertEqual(max_subarray_product([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(max_subarray_product([1]), 1)
        self.assertEqual(max_subarray_product([-1]), -1)
        self.assertEqual(max_subarray_product([0]), 0)
        self.assertEqual(max_subarray_product([-1, -2]), -1)
        self.assertEqual(max_subarray_product([2, 3, 4, 5]), 120)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(max_subarray_product([]), 0)
        self.assertEqual(max_subarray_product([1, 2, 'a']), 2)
        self.assertEqual(max_subarray_product([1, 2, None]), 2)
