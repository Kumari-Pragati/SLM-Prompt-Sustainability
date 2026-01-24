import unittest
from mbpp_49_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_typical_case(self):
        nums = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        self.assertListEqual(specified_element(nums, 1), [2, 5, 8])

    def test_edge_case_empty_list(self):
        self.assertListEqual(specified_element([], 0), [])

    def test_edge_case_empty_tuple(self):
        self.assertListEqual(specified_element([(1,)], 0), [1])

    def test_edge_case_negative_index(self):
        nums = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        with self.assertRaises(IndexError):
            specified_element(nums, -1)

    def test_edge_case_index_greater_than_len(self):
        nums = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        with self.assertRaises(IndexError):
            specified_element(nums, 3)
