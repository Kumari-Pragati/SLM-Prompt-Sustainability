import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = 2
        self.assertListEqual(func(nums, k), [3, 2])

    def test_edge_case_empty_list(self):
        nums = []
        k = 1
        self.assertListEqual(func(nums, k), [])

    def test_edge_case_single_list(self):
        nums = [[1]]
        k = 1
        self.assertListEqual(func(nums, k), [1])

    def test_edge_case_single_element(self):
        nums = [[1]]
        k = 2
        self.assertListEqual(func(nums, k), [])

    def test_edge_case_k_greater_than_nums_length(self):
        nums = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        k = len(nums) + 1
        self.assertListEqual(func(nums, k), [])

    def test_invalid_input_type_nums(self):
        with self.assertRaises(TypeError):
            func('not a list', 1)

    def test_invalid_input_type_k(self):
        with self.assertRaises(TypeError):
            func([1, 2, 3], 'not an integer')
