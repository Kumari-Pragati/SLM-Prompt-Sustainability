import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        self.assertEqual(specified_element(nums, N), [2, 5, 8])

    def test_edge_case_N_zero(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        self.assertEqual(specified_element(nums, N), [1, 4, 7])

    def test_edge_case_N_greater_than_length(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 4
        self.assertEqual(specified_element(nums, N), [])

    def test_edge_case_empty_list(self):
        nums = []
        N = 1
        self.assertEqual(specified_element(nums, N), [])

    def test_error_case_negative_N(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            specified_element(nums, N)
