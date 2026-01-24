import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(merge_sorted_list([1,3,5],[2,4,6],[7,8,9]), [1,2,3,4,5,6,7,8,9])

    def test_empty_lists(self):
        self.assertEqual(merge_sorted_list([], [], []), [])

    def test_single_element_lists(self):
        self.assertEqual(merge_sorted_list([1], [2], [3]), [1,2,3])

    def test_duplicate_elements(self):
        self.assertEqual(merge_sorted_list([1,2,2],[2,2,3],[2,3,4]), [1,2,2,2,2,2,3,3,4])

    def test_negative_numbers(self):
        self.assertEqual(merge_sorted_list([-1,-3,-5],[-2,-4,-6],[-7,-8,-9]), [-9,-8,-7,-6,-5,-4,-3,-2,-1])

    def test_mixed_numbers(self):
        self.assertEqual(merge_sorted_list([1,3,5],[2,4,6],[0,8,9]), [0,1,2,3,4,5,6,8,9])
