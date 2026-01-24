import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 2
        self.assertEqual(func(nums, k), [3, 4])

    def test_edge_case_k_equals_zero(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 0
        self.assertEqual(func(nums, k), [])

    def test_boundary_case_k_equals_one(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 1
        self.assertEqual(func(nums, k), [1])

    def test_corner_case_k_greater_than_unique_elements(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 6
        self.assertEqual(func(nums, k), [1, 2, 3, 4, 5])

    def test_corner_case_k_equals_to_number_of_unique_elements(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 5
        self.assertEqual(func(nums, k), [1, 2, 3, 4, 5])

    def test_invalid_input_negative_k(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = -1
        with self.assertRaises(Exception):
            func(nums, k)

    def test_invalid_input_non_integer_k(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 'a'
        with self.assertRaises(Exception):
            func(nums, k)
