import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_simple_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [1, 4, 7])

    def test_edge_case_empty_input(self):
        nums = []
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case_single_element_input(self):
        nums = [[1, 2, 3]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [1])

    def test_edge_case_invalid_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 10
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case_out_of_range_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        result = specified_element(nums, N)
        self.assertEqual(result, [])
