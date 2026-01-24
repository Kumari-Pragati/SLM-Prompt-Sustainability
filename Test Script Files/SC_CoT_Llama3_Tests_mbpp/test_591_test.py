import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):

    def test_typical_input(self):
        original_list = [1, 2, 3, 4, 5]
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [5, 2, 3, 4, 1])

    def test_edge_case_empty_list(self):
        original_list = []
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [])

    def test_edge_case_single_element_list(self):
        original_list = [1]
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [1])

    def test_edge_case_two_element_list(self):
        original_list = [1, 2]
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [2, 1])

    def test_edge_case_list_with_duplicates(self):
        original_list = [1, 2, 2, 3, 4, 4, 5, 5]
        swapped_list = swap_List(original_list)
        self.assertEqual(swapped_list, [5, 4, 4, 3, 2, 2, 1])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            swap_List("not a list")
