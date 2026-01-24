import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSum_Of_Subarray_Prod(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 30)

    def test_edge_case_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_edge_case_zero_length_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 0), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4, -5], 5), -30)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 30)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, 2, -3, 4, -5], 5), -10)

    def test_edge_case_large_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([100, 200, 300, 400, 500], 5), 1500)
