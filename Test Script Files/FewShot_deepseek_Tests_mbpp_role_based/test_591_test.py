import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])

    def test_single_element(self):
        self.assertEqual(swap_List([5]), [5])

    def test_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_large_list(self):
        self.assertEqual(swap_List(list(range(1, 1001))), list(range(1000, 0, -1)))

    def test_negative_numbers(self):
        self.assertEqual(swap_List([-1, -2, -3]), [-3, -2, -1])

    def test_duplicate_elements(self):
        self.assertEqual(swap_List([1, 2, 2, 1]), [1, 2, 2, 1])
