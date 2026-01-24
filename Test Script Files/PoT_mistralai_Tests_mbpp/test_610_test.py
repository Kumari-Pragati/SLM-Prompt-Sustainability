import unittest
from mbpp_610_code import remove_kth_element

class TestRemoveKthElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 2), [1, 2, 3, 4])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 5), [1, 2, 3, 4])
        self.assertEqual(remove_kth_element([1, 2, 3, 4, 5], 1), [2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_kth_element([], 1), [])

    def test_edge_case_single_element(self):
        self.assertEqual(remove_kth_element([1], 1), [])

    def test_edge_case_k_greater_than_len(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 4), [1, 2, 3])

    def test_edge_case_k_less_than_1(self):
        self.assertEqual(remove_kth_element([1, 2, 3], 0), [3])
