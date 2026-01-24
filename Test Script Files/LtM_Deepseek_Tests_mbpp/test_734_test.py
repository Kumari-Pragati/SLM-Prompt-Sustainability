import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3], 3), 20)
        self.assertEqual(sum_Of_Subarray_Prod([1, 3, 3], 3), 18)

    def test_edge_conditions(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)
        self.assertEqual(sum_Of_Subarray_Prod([1], 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(sum_Of_Subarray_Prod([1000000000], 1), 1000000000)
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3], 3), -20)

    def test_complex_cases(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5], 5), 40)
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6], 6), 70)
