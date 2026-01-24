import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_neg([-1, 2, 3, 4, 5]), -1)

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, largest_neg, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(largest_neg([-1]), -1)

    def test_edge_case_all_positive_list(self):
        self.assertEqual(largest_neg([1, 2, 3, 4, 5]), None)

    def test_edge_case_all_negative_list(self):
        self.assertEqual(largest_neg([-1, -2, -3, -4, -5]), -5)

    def test_edge_case_mixed_list(self):
        self.assertEqual(largest_neg([-1, 2, 3, -4, 5]), -4)
