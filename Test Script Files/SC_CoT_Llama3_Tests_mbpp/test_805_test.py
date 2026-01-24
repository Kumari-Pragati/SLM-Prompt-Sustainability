import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])

    def test_edge_case_empty_list(self):
        self.assertRaises(ValueError, max_sum_list, [])

    def test_edge_case_single_list(self):
        self.assertEqual(max_sum_list([[1, 2, 3]]), [1, 2, 3])

    def test_edge_case_all_empty_lists(self):
        self.assertEqual(max_sum_list([[], [], []]), [])

    def test_edge_case_all_single_element_lists(self):
        self.assertEqual(max_sum_list([[1], [2], [3]]), [1, 2, 3])

    def test_edge_case_all_equal_lists(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), [1, 2, 3])

    def test_edge_case_mixed_lists(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            max_sum_list("not a list")

    def test_invalid_input_non_list_of_lists(self):
        with self.assertRaises(TypeError):
            max_sum_list([[1, 2, 3], "not a list"])
