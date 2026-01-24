import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_swap_list_typical_case(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])

    def test_swap_list_single_element(self):
        self.assertEqual(swap_List([5]), [5])

    def test_swap_list_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_swap_list_two_elements(self):
        self.assertEqual(swap_List([10, 20]), [20, 10])
