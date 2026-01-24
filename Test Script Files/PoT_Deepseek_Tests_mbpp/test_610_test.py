import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 3), [1, 2, 4, 5])

    def test_edge_case_first_element(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [2, 3, 4, 5])

    def test_edge_case_last_element(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])

    def test_boundary_case_empty_list(self):
        self.assertEqual(remove_kth_element([], 1), [])

    def test_boundary_case_single_element_list(self):
        self.assertEqual(remove_kth_element([1], 1), [])

    def test_invalid_k_greater_than_length(self):
        with self.assertRaises(IndexError):
            remove_kth_element([1, 2, 3, 4, 5], 6)

    def test_invalid_k_less_than_1(self):
        with self.assertRaises(IndexError):
            remove_kth_element([1, 2, 3, 4, 5], 0)
