import unittest
from mbpp_734_code import sum_Of_Subarray_Prod

class TestSumOfSubarrayProd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Of_Subarray_Prod([1, 2, 3, 4], 4), 50)

    def test_single_element(self):
        self.assertEqual(sum_Of_Subarray_Prod([5], 1), 5)

    def test_empty_array(self):
        self.assertEqual(sum_Of_Subarray_Prod([], 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([-1, -2, -3, -4], 4), -50)

    def test_zeroes(self):
        self.assertEqual(sum_Of_Subarray_Prod([0, 0, 0, 0], 4), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_Of_Subarray_Prod([10**6]*4, 4), 4*10**12)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Of_Subarray_Prod("not an array", 7)
