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
        self.assertEqual(merge_sorted_list([1,2,2],[2,3,4],[2,5,6]), [1,2,2,2,2,3,4,5,6])

    def test_negative_numbers(self):
        self.assertEqual(merge_sorted_list([-5,-3,-1],[0,2,4],[1,3,5]), [-5,-3,-1,0,1,2,3,4,5])

    def test_large_numbers(self):
        self.assertEqual(merge_sorted_list([1000,2000,3000],[4000,5000,6000],[7000,8000,9000]), [1000,2000,3000,4000,5000,6000,7000,8000,9000])
