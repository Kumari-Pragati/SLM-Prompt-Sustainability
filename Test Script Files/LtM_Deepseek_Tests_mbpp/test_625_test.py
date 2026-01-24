import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_simple_list(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])

    def test_swap_single_element_list(self):
        self.assertEqual(swap_List([5]), [5])

    def test_swap_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_large_list(self):
        self.assertEqual(swap_List(list(range(1, 1001))), list(range(1000, 0, -1)))

    def test_swap_list_with_duplicates(self):
        self.assertEqual(swap_List([1, 2, 2, 1]), [1, 2, 2, 1])

    def test_swap_list_with_negative_numbers(self):
        self.assertEqual(swap_List([-1, -2, -3]), [-3, -2, -1])

    def test_swap_list_with_zero(self):
        self.assertEqual(swap_List([0]), [0])
