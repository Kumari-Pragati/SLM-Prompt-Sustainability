import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):
    def test_typical_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 1
        self.assertEqual(specified_element(nums, N), [1, 4, 7])

    def test_edge_case(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 0
        self.assertEqual(specified_element(nums, N), [1, 4, 7])

    def test_edge_case2(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = 2
        self.assertEqual(specified_element(nums, N), [3, 6, 9])

    def test_invalid_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        N = -1
        with self.assertRaises(IndexError):
            specified_element(nums, N)

    def test_empty_list(self):
        nums = []
        N = 0
        self.assertEqual(specified_element(nums, N), [])

    def test_single_element_list(self):
        nums = [[1, 2, 3]]
        N = 1
        self.assertEqual(specified_element(nums, N), [3])
