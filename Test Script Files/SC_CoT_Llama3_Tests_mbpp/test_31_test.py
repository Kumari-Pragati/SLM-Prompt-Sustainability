import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_typical_input(self):
        nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        k = 3
        self.assertEqual(func(nums, k), [1, 2, 3])

    def test_edge_case_k_zero(self):
        nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        k = 0
        self.assertEqual(func(nums, k), [])

    def test_edge_case_k_greater_than_length(self):
        nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        k = 10
        self.assertEqual(func(nums, k), [1, 2, 3])

    def test_edge_case_empty_input(self):
        nums = []
        k = 3
        self.assertEqual(func(nums, k), [])

    def test_edge_case_k_is_one(self):
        nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        k = 1
        self.assertEqual(func(nums, k), [1])

    def test_invalid_input_non_integer_k(self):
        nums = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        k = 'a'
        with self.assertRaises(TypeError):
            func(nums, k)

    def test_invalid_input_non_list_input(self):
        nums = 'abc'
        k = 3
        with self.assertRaises(TypeError):
            func(nums, k)
