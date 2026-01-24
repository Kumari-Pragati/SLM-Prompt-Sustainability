import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_list_typical_case(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])

    def test_swap_list_single_element(self):
        self.assertEqual(swap_List([5]), [5])

    def test_swap_list_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_list_two_elements(self):
        self.assertEqual(swap_List([10, 20]), [20, 10])

    def test_swap_list_large_list(self):
        large_list = list(range(1, 1001))
        self.assertEqual(swap_List(large_list), list(range(1000, 0, -1)))
