import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_list_empty(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_list_single_element(self):
        self.assertEqual(swap_List([1]), [1])

    def test_swap_list_two_elements(self):
        self.assertEqual(swap_List([1, 2]), [2, 1])

    def test_swap_list_three_elements(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])

    def test_swap_list_large(self):
        self.assertEqual(swap_List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_swap_list_negative_numbers(self):
        self.assertEqual(swap_List([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])
