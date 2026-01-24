import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_swap_list_with_even_length(self):
        original_list = [1, 2, 3, 4]
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [4, 2, 3, 1])

    def test_swap_list_with_odd_length(self):
        original_list = [1, 2, 3, 4, 5]
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [5, 2, 3, 4, 1])

    def test_swap_list_with_empty_list(self):
        original_list = []
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [])

    def test_swap_list_with_single_element_list(self):
        original_list = [1]
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [1])

    def test_swap_list_with_non_list_input(self):
        with self.assertRaises(TypeError):
            swap_List("not a list")
