import unittest
from mbpp_625_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_swap_list_typical(self):
        original_list = [1, 2, 3, 4, 5]
        expected_list = [5, 2, 3, 4, 1]
        self.assertEqual(swap_List(original_list), expected_list)

    def test_swap_list_edge_case_empty(self):
        original_list = []
        expected_list = []
        self.assertEqual(swap_List(original_list), expected_list)

    def test_swap_list_edge_case_single_element(self):
        original_list = [1]
        expected_list = [1]
        self.assertEqual(swap_List(original_list), expected_list)

    def test_swap_list_edge_case_two_elements(self):
        original_list = [1, 2]
        expected_list = [2, 1]
        self.assertEqual(swap_List(original_list), expected_list)

    def test_swap_list_edge_case_three_elements(self):
        original_list = [1, 2, 3]
        expected_list = [3, 2, 1]
        self.assertEqual(swap_List(original_list), expected_list)

    def test_swap_list_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            swap_List("not a list")
