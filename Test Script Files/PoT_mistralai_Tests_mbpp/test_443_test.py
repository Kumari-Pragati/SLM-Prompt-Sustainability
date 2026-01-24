import unittest
from443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_neg([-5, -3, -2, 0, 1]), -5)
        self.assertEqual(largest_neg([-10, -5, 0, 2, 10]), -10)
        self.assertEqual(largest_neg([-1, 0, 1]), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(largest_neg([]), None)

    def test_edge_case_single_element(self):
        self.assertEqual(largest_neg([1]), -1)
        self.assertEqual(largest_neg([-1]), -1)

    def test_edge_case_all_zero(self):
        self.assertEqual(largest_neg([0, 0, 0]), 0)

    def test_edge_case_all_positive(self):
        self.assertEqual(largest_neg([1, 2, 3]), None)
