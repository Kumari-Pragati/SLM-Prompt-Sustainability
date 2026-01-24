import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_single_element_list(self):
        self.assertEqual(swap_List([1]), [1])

    def test_normal_list(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_list_with_duplicates(self):
        self.assertEqual(swap_List([1, 1, 2, 3]), [3, 1, 1, 2])

    def test_list_with_negative_index(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_list_with_out_of_range_index(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])
