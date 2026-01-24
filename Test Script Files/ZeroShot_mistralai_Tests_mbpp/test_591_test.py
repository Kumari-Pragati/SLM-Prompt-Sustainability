import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_single_element_list(self):
        self.assertEqual(swap_List([1]), [1])

    def test_two_elements_list(self):
        self.assertEqual(swap_List([1, 2]), [2, 1])

    def test_multiple_elements_list(self):
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 1, 2, 3])

    def test_negative_index(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_list_with_non_integer_elements(self):
        self.assertEqual(swap_List([1, 'a', 3]), ['a', 1, 3])
