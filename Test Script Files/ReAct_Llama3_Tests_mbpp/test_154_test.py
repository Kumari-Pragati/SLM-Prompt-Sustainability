import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_typical_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [1, 4, 7])

    def test_edge_case_N_zero(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        with self.assertRaises(IndexError):
            specified_element(nums, N)

    def test_edge_case_N_out_of_range(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        result = specified_element(nums, N)
        self.assertEqual(result, [3, 6, 9])

    def test_edge_case_N_negative(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            specified_element(nums, N)

    def test_empty_list(self):
        nums = []
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [])
