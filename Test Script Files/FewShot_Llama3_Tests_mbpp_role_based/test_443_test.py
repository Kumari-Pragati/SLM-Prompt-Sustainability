import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(largest_neg([-10, -5, 0, 5, 10]), -10)

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, largest_neg, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(largest_neg([-10]), -10)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(largest_neg([-10, -5, -5, 0, 5]), -10)

    def test_edge_case_list_with_no_negative_numbers(self):
        self.assertEqual(largest_neg([0, 1, 2, 3, 4]), 0)

    def test_edge_case_list_with_no_numbers(self):
        self.assertRaises(TypeError, largest_neg, ['a', 'b', 'c'])
