import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(swap_List([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])

    def test_edge_case_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(swap_List([1]), [1])

    def test_edge_case_two_element_list(self):
        self.assertEqual(swap_List([1, 2]), [2, 1])

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(swap_List([1, 2, 2, 3, 1]), [1, 2, 2, 1, 3])

    def test_edge_case_list_with_duplicates_and_empty(self):
        self.assertEqual(swap_List([1, 2, 2, 3, 1, 0]), [0, 2, 2, 1, 3, 1])

    def test_edge_case_list_with_duplicates_and_empty_and_single(self):
        self.assertEqual(swap_List([1, 2, 2, 3, 1, 0, 1]), [1, 2, 2, 0, 1, 3, 1])
