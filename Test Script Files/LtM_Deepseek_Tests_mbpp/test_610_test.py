import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 3), [1, 2, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_kth_element([], 3), [])

    def test_edge_case_k_equals_1(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [2, 3, 4, 5])

    def test_edge_case_k_equals_length(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5])

    def test_edge_case_k_less_than_1(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
