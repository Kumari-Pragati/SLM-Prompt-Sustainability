import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_list([(1,2,3), (4,5,6), (7,8,9)]), '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]')

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_list([]), '[]')

    def test_edge_case_single_element_list(self):
        self.assertEqual(sort_list([(1,2,3)]), '[[1, 2, 3]]')

    def test_edge_case_single_element_list_with_duplicates(self):
        self.assertEqual(sort_list([(1,2,3), (1,2,3)]), '[[1, 2, 3], [1, 2, 3]]')

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sort_list([(-1,-2,-3), (4,5,6), (7,8,9)]), '[[(-1, -2, -3),], [4, 5, 6], [7, 8, 9]]')

    def test_edge_case_zero(self):
        self.assertEqual(sort_list([(0,0,0), (4,5,6), (7,8,9)]), '[[0, 0, 0], [4, 5, 6], [7, 8, 9]]')

    def test_edge_case_max_length(self):
        self.assertEqual(sort_list([(1,2,3,4,5,6,7,8,9,10), (11,12,13,14,15,16,17,18,19,20)]), '[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]')
