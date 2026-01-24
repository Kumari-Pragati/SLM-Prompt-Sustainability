import unittest
from mbpp_101_code import kth_element

class TestKthElement(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 3), 3)

    def test_edge_case_k_equal_to_n(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 5), 5)

    def test_edge_case_k_equal_to_1(self):
        self.assertEqual(kth_element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_case_n_equal_to_1(self):
        self.assertEqual(kth_element([1], 1, 1), 1)

    def test_edge_case_n_equal_to_2(self):
        self.assertEqual(kth_element([1, 2], 2, 1), 1)

    def test_edge_case_k_greater_than_n(self):
        with self.assertRaises(IndexError):
            kth_element([1, 2, 3, 4, 5], 5, 6)

    def test_edge_case_k_less_than_1(self):
        with self.assertRaises(IndexError):
            kth_element([1, 2, 3, 4, 5], 5, 0)

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            kth_element([], 0, 1)

    def test_edge_case_array_with_duplicates(self):
        self.assertEqual(kth_element([1, 2, 2, 3, 4, 5], 6, 3), 3)

    def test_edge_case_array_with_duplicates_and_k_equal_to_n(self):
        self.assertEqual(kth_element([1, 2, 2, 3, 4, 5], 6, 6), 5)

    def test_edge_case_array_with_duplicates_and_k_equal_to_1(self):
        self.assertEqual(kth_element([1, 2, 2, 3, 4, 5], 6, 1), 1)
