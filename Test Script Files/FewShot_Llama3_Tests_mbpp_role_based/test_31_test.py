import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        k = 3
        self.assertEqual(func(nums, k), [5, 4, 3])

    def test_edge_case_k_zero(self):
        nums = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        k = 0
        self.assertEqual(func(nums, k), [])

    def test_edge_case_k_greater_than_length(self):
        nums = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        k = 10
        self.assertEqual(func(nums, k), [5, 4, 3, 2, 1])

    def test_invalid_input_non_integer_k(self):
        nums = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        k = 'a'
        with self.assertRaises(TypeError):
            func(nums, k)

    def test_invalid_input_non_list_nums(self):
        nums = 'abc'
        k = 3
        with self.assertRaises(TypeError):
            func(nums, k)
