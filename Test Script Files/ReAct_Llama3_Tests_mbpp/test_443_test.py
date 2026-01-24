import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10]), -10)

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, largest_neg, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(largest_neg([-10]), -10)

    def test_edge_case_single_negative_element_list(self):
        self.assertEqual(largest_neg([-10, 0, 5, 10]), -10)

    def test_edge_case_single_positive_element_list(self):
        self.assertEqual(largest_neg([10, 5, 0, -10]), -10)

    def test_edge_case_all_negative_elements_list(self):
        self.assertEqual(largest_neg([-10, -5, -3, -1]), -10)

    def test_edge_case_all_positive_elements_list(self):
        self.assertEqual(largest_neg([10, 5, 3, 1]), 1)

    def test_edge_case_mixed_elements_list(self):
        self.assertEqual(largest_neg([-10, 0, 5, 10, -5]), -10)
