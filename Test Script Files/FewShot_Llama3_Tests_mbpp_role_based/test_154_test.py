import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        result = specified_element(nums, N)
        self.assertEqual(result, [2, 5, 8])

    def test_edge_case_empty_list(self):
        nums = []
        N = 0
        result = specified_element(nums, N)
        self.assertEqual(result, [])

    def test_edge_case_single_element_list(self):
        nums = [[1, 2, 3]]
        N = 0
        result = specified_element(nums, N)
        self.assertEqual(result, [1])

    def test_edge_case_invalid_N(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 10
        with self.assertRaises(IndexError):
            specified_element(nums, N)
