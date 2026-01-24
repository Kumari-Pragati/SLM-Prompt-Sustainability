import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 3), [1, 2, 3, 5])

    def test_edge_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])

    def test_edge_case_zero(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])

    def test_edge_case_negative(self):
        with self.assertRaises(IndexError):
            remove_kth_element([1, 2, 3, 4, 5], -1)

    def test_edge_case_greater_than_length(self):
        with self.assertRaises(IndexError):
            remove_kth_element([1, 2, 3, 4, 5], 6)

    def test_typical_case_empty_list(self):
        self.assertEqual(remove_kth_element([], 1), [])

    def test_typical_case_single_element(self):
        self.assertEqual(remove_kth_element([1], 1), [])

    def test_typical_case_single_element_k_zero(self):
        self.assertEqual(remove_kth_element([1], 0), [1])

    def test_typical_case_single_element_k_greater_than_length(self):
        with self.assertRaises(IndexError):
            remove_kth_element([1], 2)
