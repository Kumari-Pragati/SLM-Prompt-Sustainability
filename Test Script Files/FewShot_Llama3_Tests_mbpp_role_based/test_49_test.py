import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [2, 5, 8])

    def test_edge_case_empty_list(self):
        nums = []
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        nums = [[1, 2, 3]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [2])

    def test_edge_case_N_out_of_range(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 10
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case_N_negative(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        result = specified_element(nums, N)
        self.assertEqual(result, [])
