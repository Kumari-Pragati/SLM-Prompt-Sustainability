import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_list_with_two_elements(self):
        self.assertEqual(swap_List([1, 2]), [2, 1])

    def test_swap_list_with_three_elements(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])

    def test_swap_list_with_single_element(self):
        self.assertEqual(swap_List([1]), [1])

    def test_swap_list_with_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_list_with_negative_numbers(self):
        self.assertEqual(swap_List([-1, -2]), [-2, -1])

    def test_swap_list_with_zero(self):
        self.assertEqual(swap_List([0, 1]), [1, 0])
