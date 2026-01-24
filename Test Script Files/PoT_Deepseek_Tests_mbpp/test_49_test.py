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

    def test_edge_case_N_last_index(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        self.assertEqual(specified_element(nums, N), [3, 6, 9])

    def test_corner_case_empty_list(self):
        nums = []
        N = 0
        self.assertEqual(specified_element(nums, N), [])

    def test_corner_case_single_element(self):
        nums = [[1]]
        N = 0
        self.assertEqual(specified_element(nums, N), [1])

    def test_corner_case_N_greater_than_length(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 3
        self.assertEqual(specified_element(nums, N), [3, 6, 9])
